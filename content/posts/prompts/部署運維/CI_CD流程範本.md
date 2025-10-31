+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = 'CI_CD流程範本'
tags = ['prompts', '部署運維']
categories = ['prompts']
+++
# CI/CD 流程範本

## Prompt 目標

指導 AI 建立完整的 CI/CD 流程，包含持續整合、持續部署和基礎設施即程式碼。

## 角色設定

你是一位資深 DevOps 工程師，具備豐富的 CI/CD 流程設計和實作經驗，熟悉各種自動化部署工具和雲端平台。

## 任務描述

請協助我為 {專案名稱} 建立完整的 CI/CD 流程。

### 專案 DevOps 背景

- **專案名稱**: {填入專案名稱}
- **應用架構**: {填入應用架構，如：微服務、單體應用}
- **技術棧**: {填入技術棧}
- **部署平台**: {填入目標平台，如：AWS、Azure、GCP、Kubernetes}
- **團隊規模**: {填入團隊人數}
- **發布頻率**: {填入預期發布頻率}

### CI/CD 設計要求

請按照以下結構設計 CI/CD 流程：

#### 1. 持續整合設計
- 原始碼管理策略
- 建置流程設計
- 自動化測試整合
- 程式碼品質門檻

#### 2. 持續部署設計
- 部署策略選擇
- 環境管理規劃
- 發布流程設計
- 回退機制設計

#### 3. 基礎設施管理
- 基礎設施即程式碼
- 環境配置管理
- 監控和告警設置
- 安全性配置

#### 4. 自動化工具整合
- CI/CD 工具選擇
- 容器化策略
- 編排工具配置
- 工具鏈整合

#### 5. 品質和安全
- 程式碼掃描整合
- 漏洞檢測流程
- 合規性檢查
- 稽核日誌管理

#### 6. 監控和運維
- 應用程式監控
- 基礎設施監控
- 日誌聚合分析
- 事件響應流程

## 輸出格式

```markdown
# {專案名稱} CI/CD 流程設計

## 1. 流程概覽

### 1.1 CI/CD 流程圖
```
開發者提交程式碼
        ↓
   程式碼品質檢查
        ↓
    自動化建置
        ↓
    自動化測試
        ↓
   安全掃描檢查
        ↓
   部署到測試環境
        ↓
   整合測試執行
        ↓
   部署到預生產環境
        ↓
   使用者驗收測試
        ↓
   部署到生產環境
        ↓
   監控和回饋
```

### 1.2 分支策略
**採用策略:** GitFlow
**分支結構:**
- `main`: 生產環境程式碼
- `develop`: 開發整合分支
- `feature/*`: 功能開發分支
- `release/*`: 發布準備分支
- `hotfix/*`: 緊急修正分支

### 1.3 部署策略
**選擇策略:** 藍綠部署 (Blue-Green Deployment)
**優勢:**
- 零停機時間部署
- 快速回退能力
- 完整的預生產驗證
- 風險最小化

## 2. 持續整合流程

### 2.1 GitHub Actions 工作流程

#### 主要建置流程
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

env:
  JAVA_VERSION: '17'
  NODE_VERSION: '18'
  DOCKER_REGISTRY: your-registry.com

jobs:
  code-quality:
    name: 程式碼品質檢查
    runs-on: ubuntu-latest
    steps:
    - name: Checkout 程式碼
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: 設定 Java
      uses: actions/setup-java@v3
      with:
        java-version: ${{ env.JAVA_VERSION }}
        distribution: 'temurin'

    - name: 快取 Maven 相依性
      uses: actions/cache@v3
      with:
        path: ~/.m2
        key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}

    - name: 執行 CheckStyle
      run: mvn checkstyle:check

    - name: 執行 SpotBugs
      run: mvn spotbugs:check

    - name: SonarQube 掃描
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      run: mvn sonar:sonar

  unit-tests:
    name: 單元測試
    runs-on: ubuntu-latest
    needs: code-quality
    steps:
    - name: Checkout 程式碼
      uses: actions/checkout@v4

    - name: 設定 Java
      uses: actions/setup-java@v3
      with:
        java-version: ${{ env.JAVA_VERSION }}
        distribution: 'temurin'

    - name: 執行單元測試
      run: mvn test

    - name: 產生測試報告
      run: mvn jacoco:report

    - name: 上傳覆蓋率報告
      uses: codecov/codecov-action@v3
      with:
        file: target/site/jacoco/jacoco.xml

  build-and-push:
    name: 建置和推送映像檔
    runs-on: ubuntu-latest
    needs: [code-quality, unit-tests]
    if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/develop'
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
      image-digest: ${{ steps.build.outputs.digest }}
    steps:
    - name: Checkout 程式碼
      uses: actions/checkout@v4

    - name: 設定 Java
      uses: actions/setup-java@v3
      with:
        java-version: ${{ env.JAVA_VERSION }}
        distribution: 'temurin'

    - name: 建置應用程式
      run: mvn clean package -DskipTests

    - name: 設定 Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: 登入 Container Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.DOCKER_REGISTRY }}
        username: ${{ secrets.REGISTRY_USERNAME }}
        password: ${{ secrets.REGISTRY_PASSWORD }}

    - name: 提取中繼資料
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.DOCKER_REGISTRY }}/myapp
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}

    - name: 建置和推送 Docker 映像檔
      id: build
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  security-scan:
    name: 安全性掃描
    runs-on: ubuntu-latest
    needs: build-and-push
    steps:
    - name: 執行 Trivy 漏洞掃描
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: ${{ needs.build-and-push.outputs.image-tag }}
        format: 'sarif'
        output: 'trivy-results.sarif'

    - name: 上傳 Trivy 掃描結果
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'

  deploy-test:
    name: 部署到測試環境
    runs-on: ubuntu-latest
    needs: [build-and-push, security-scan]
    if: github.ref == 'refs/heads/develop'
    environment: test
    steps:
    - name: 部署到測試環境
      run: |
        echo "部署映像檔 ${{ needs.build-and-push.outputs.image-tag }} 到測試環境"
        # 實際部署邏輯

  integration-tests:
    name: 整合測試
    runs-on: ubuntu-latest
    needs: deploy-test
    steps:
    - name: Checkout 程式碼
      uses: actions/checkout@v4

    - name: 設定 Java
      uses: actions/setup-java@v3
      with:
        java-version: ${{ env.JAVA_VERSION }}
        distribution: 'temurin'

    - name: 執行整合測試
      run: mvn verify -Dgroups=integration
      env:
        TEST_BASE_URL: https://test.myapp.com

  deploy-production:
    name: 部署到生產環境
    runs-on: ubuntu-latest
    needs: [build-and-push, security-scan]
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
    - name: 部署到生產環境
      run: |
        echo "部署映像檔 ${{ needs.build-and-push.outputs.image-tag }} 到生產環境"
        # 實際部署邏輯
```

### 2.2 品質門檻設定

#### SonarQube 品質門檻
```yaml
quality_gate:
  conditions:
    - metric: coverage
      operator: GREATER_THAN
      value: 80
    - metric: duplicated_lines_density
      operator: LESS_THAN
      value: 3
    - metric: maintainability_rating
      operator: LESS_THAN
      value: 3
    - metric: reliability_rating
      operator: LESS_THAN
      value: 3
    - metric: security_rating
      operator: LESS_THAN
      value: 3
```

## 3. 容器化配置

### 3.1 Dockerfile 最佳實務

```dockerfile
# 多階段建置 Dockerfile
# 建置階段
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn clean package -DskipTests

# 執行階段
FROM eclipse-temurin:17-jre-alpine AS runtime

# 建立非 root 使用者
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup

# 安裝必要的套件
RUN apk add --no-cache curl jq

# 設定工作目錄
WORKDIR /app

# 複製應用程式
COPY --from=build /app/target/*.jar app.jar

# 變更擁有者
RUN chown -R appuser:appgroup /app

# 切換到非 root 使用者
USER appuser

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

# 暴露埠口
EXPOSE 8080

# 啟動應用程式
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### 3.2 Docker Compose 開發環境

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=development
      - DB_HOST=postgres
      - REDIS_HOST=redis
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - app-network

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser -d myapp"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - app-network

volumes:
  postgres_data:
  redis_data:

networks:
  app-network:
    driver: bridge
```

## 4. Kubernetes 部署配置

### 4.1 應用程式部署配置

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
    version: "1.0"
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: your-registry.com/myapp:latest
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: "production"
        - name: DB_HOST
          value: "postgres-service"
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          initialDelaySeconds: 60
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /actuator/health/readiness
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        volumeMounts:
        - name: config-volume
          mountPath: /app/config
      volumes:
      - name: config-volume
        configMap:
          name: myapp-config

---
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP

---
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-service
            port:
              number: 80
```

### 4.2 Helm Chart 配置

```yaml
# Chart.yaml
apiVersion: v2
name: myapp
description: A Helm chart for MyApp
type: application
version: 0.1.0
appVersion: "1.0.0"

# values.yaml
replicaCount: 3

image:
  repository: your-registry.com/myapp
  pullPolicy: IfNotPresent
  tag: "latest"

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  className: "nginx"
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
  hosts:
    - host: myapp.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: myapp-tls
      hosts:
        - myapp.example.com

resources:
  limits:
    cpu: 500m
    memory: 1Gi
  requests:
    cpu: 250m
    memory: 512Mi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 80

monitoring:
  enabled: true
  serviceMonitor:
    enabled: true
```

## 5. 基礎設施即程式碼

### 5.1 Terraform 配置

```hcl
# main.tf
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket = "myapp-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "ap-southeast-1"
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "Terraform"
    }
  }
}

# VPC 配置
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  
  name = "${var.project_name}-vpc"
  cidr = var.vpc_cidr
  
  azs             = var.availability_zones
  private_subnets = var.private_subnet_cidrs
  public_subnets  = var.public_subnet_cidrs
  
  enable_nat_gateway = true
  enable_vpn_gateway = false
  
  tags = {
    Environment = var.environment
  }
}

# EKS 叢集
module "eks" {
  source = "terraform-aws-modules/eks/aws"
  
  cluster_name    = "${var.project_name}-eks"
  cluster_version = "1.27"
  
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets
  
  eks_managed_node_groups = {
    main = {
      min_size     = 1
      max_size     = 5
      desired_size = 3
      
      instance_types = ["t3.medium"]
      capacity_type  = "ON_DEMAND"
    }
  }
  
  tags = {
    Environment = var.environment
  }
}

# RDS 資料庫
resource "aws_db_instance" "main" {
  identifier = "${var.project_name}-db"
  
  engine         = "postgres"
  engine_version = "15.3"
  instance_class = "db.t3.micro"
  
  allocated_storage     = 20
  max_allocated_storage = 100
  
  db_name  = var.db_name
  username = var.db_username
  password = var.db_password
  
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name
  
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  skip_final_snapshot = false
  final_snapshot_identifier = "${var.project_name}-db-final-snapshot"
  
  tags = {
    Name = "${var.project_name}-database"
  }
}
```

### 5.2 Ansible Playbook

```yaml
# deploy.yml
---
- name: 部署應用程式到 Kubernetes
  hosts: localhost
  gather_facts: false
  vars:
    app_name: myapp
    namespace: production
    image_tag: "{{ ansible_env.IMAGE_TAG | default('latest') }}"
    
  tasks:
    - name: 建立 namespace
      kubernetes.core.k8s:
        name: "{{ namespace }}"
        api_version: v1
        kind: Namespace
        state: present
        
    - name: 套用 ConfigMap
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: v1
          kind: ConfigMap
          metadata:
            name: "{{ app_name }}-config"
            namespace: "{{ namespace }}"
          data:
            application.properties: |
              server.port=8080
              spring.datasource.url=jdbc:postgresql://postgres-service:5432/myapp
              logging.level.com.myapp=INFO
              
    - name: 部署應用程式
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: apps/v1
          kind: Deployment
          metadata:
            name: "{{ app_name }}"
            namespace: "{{ namespace }}"
          spec:
            replicas: 3
            selector:
              matchLabels:
                app: "{{ app_name }}"
            template:
              metadata:
                labels:
                  app: "{{ app_name }}"
              spec:
                containers:
                - name: "{{ app_name }}"
                  image: "your-registry.com/{{ app_name }}:{{ image_tag }}"
                  ports:
                  - containerPort: 8080
                  
    - name: 等待部署完成
      kubernetes.core.k8s_info:
        api_version: apps/v1
        kind: Deployment
        name: "{{ app_name }}"
        namespace: "{{ namespace }}"
        wait: true
        wait_condition:
          type: Progressing
          status: "True"
          reason: NewReplicaSetAvailable
        wait_timeout: 600
```

## 6. 監控和告警

### 6.1 Prometheus 配置

```yaml
# prometheus-config.yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'myapp'
    kubernetes_sd_configs:
    - role: pod
    relabel_configs:
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
      action: replace
      target_label: __metrics_path__
      regex: (.+)

alerting:
  alertmanagers:
  - static_configs:
    - targets:
      - alertmanager:9093

rule_files:
  - "alert_rules.yml"
```

### 6.2 告警規則

```yaml
# alert_rules.yml
groups:
- name: myapp.rules
  rules:
  - alert: HighErrorRate
    expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "高錯誤率檢測"
      description: "應用程式錯誤率超過 10%"

  - alert: HighCPUUsage
    expr: cpu_usage_percent > 80
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "CPU 使用率過高"
      description: "CPU 使用率超過 80%"

  - alert: LowDiskSpace
    expr: disk_free_percent < 20
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "磁碟空間不足"
      description: "可用磁碟空間少於 20%"
```

## 7. 安全性配置

### 7.1 安全掃描流程

```yaml
# security-scan.yml
name: 安全性掃描

on:
  schedule:
    - cron: '0 2 * * *'  # 每日凌晨 2 點執行
  push:
    branches: [ main ]

jobs:
  dependency-check:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: 執行 OWASP Dependency Check
      uses: dependency-check/Dependency-Check_Action@main
      with:
        project: 'myapp'
        path: '.'
        format: 'ALL'
        
    - name: 上傳掃描結果
      uses: actions/upload-artifact@v3
      with:
        name: dependency-check-report
        path: reports/

  docker-security-scan:
    runs-on: ubuntu-latest
    steps:
    - name: 執行 Docker 安全掃描
      run: |
        docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
          aquasec/trivy image your-registry.com/myapp:latest
```

### 7.2 Kubernetes 安全政策

```yaml
# security-policy.yaml
apiVersion: v1
kind: SecurityContextConstraints
metadata:
  name: myapp-scc
allowHostDirVolumePlugin: false
allowHostIPC: false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegedContainer: false
allowedCapabilities: []
defaultAddCapabilities: []
requiredDropCapabilities:
- KILL
- MKNOD
- SETUID
- SETGID
runAsUser:
  type: MustRunAsRange
  uidRangeMin: 1001
  uidRangeMax: 2000
seLinuxContext:
  type: MustRunAs
volumes:
- configMap
- downwardAPI
- emptyDir
- persistentVolumeClaim
- projected
- secret
```
```

## CI/CD 最佳實務

### 流程設計原則
- **快速回饋**: 盡早發現問題
- **自動化優先**: 減少人工干預
- **漸進式部署**: 降低部署風險
- **可觀測性**: 全面監控和日誌

### 安全性考量
- **最小權限原則**: 只給予必要的權限
- **密鑰管理**: 使用專用的密鑰管理服務
- **映像檔掃描**: 定期掃描容器映像檔
- **網路隔離**: 適當的網路分段

### 效能最佳化
- **平行執行**: 平行化測試和建置步驟
- **快取策略**: 有效利用建置快取
- **增量建置**: 只建置變更的部分
- **資源管理**: 合理分配運算資源

## 品質檢查清單

- [ ] CI/CD 流程設計完整
- [ ] 自動化測試整合完善
- [ ] 安全掃描機制健全
- [ ] 部署策略合理可行
- [ ] 監控告警配置完整
- [ ] 回退機制設計明確
- [ ] 環境配置管理規範
- [ ] 文檔和培訓完整
- [ ] 效能和可靠性達標
- [ ] 合規性要求滿足

## 使用範例

### 部署命令範例

```bash
# 手動觸發部署
gh workflow run "CI/CD Pipeline" --ref main

# 使用 Helm 部署
helm upgrade --install myapp ./helm-chart \
  --namespace production \
  --set image.tag=v1.2.3

# 使用 kubectl 部署
kubectl apply -f k8s/manifests/ -n production

# 檢查部署狀態
kubectl rollout status deployment/myapp -n production
```

### 監控指令範例

```bash
# 查看應用程式日誌
kubectl logs -f deployment/myapp -n production

# 查看 Pod 狀態
kubectl get pods -l app=myapp -n production

# 查看資源使用情況
kubectl top pods -n production
```

## 注意事項

1. 確保 CI/CD 流程的安全性和穩定性
2. 建立完善的測試和驗收機制
3. 實作有效的監控和告警系統
4. 定期檢視和最佳化流程效率
5. 培養團隊的 DevOps 技能和文化
6. 建立清楚的故障排除和回復程序
