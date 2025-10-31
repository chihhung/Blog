+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = '12-Factor App 說明與對應解決方案'
tags = ['指引', '設計開發']
categories = ['指引']
+++
1. Codebase（單一程式碼庫，多個部署環境）

原則：一個應用程式應有單一程式碼庫，透過不同的部署（deploy）對應不同環境（dev/test/prod）。
解決方案：
   - 使用 GitLab repository 管理專案。
   - 每個環境使用不同 branch 或 tag（如 develop, release, main）。
   - CI/CD pipeline 進行自動化部署，避免分散程式碼庫。

2. Dependencies（明確宣告與隔離依賴）

原則：應用程式必須明確管理相依性，避免依賴系統環境。
解決方案：
   - 後端：使用 Maven pom.xml 宣告所有 dependencies，不依賴本地安裝的 jar。
   - 前端：使用 package.json 鎖定依賴版本。
   - 建議使用 Docker 建立一致的 build/runtime 環境。

3. Config（將設定與程式碼分離）

原則：設定（如 DB 密碼、API key）不應寫死在程式碼中。
解決方案：
   - Spring Boot 使用 application.yml + 外部設定檔 或 環境變數。
   - GitLab CI/CD 提供 Environment Variables 管理不同環境的設定。
   - 建議搭配 Vault / AWS Secrets Manager / Kubernetes Secrets。

4. Backing Services（後端服務當作附加資源）

原則：資料庫、快取、MQ、外部 API 都應視為「可替換的資源」。
解決方案：
   - DB（MySQL/DB2/PostgreSQL）、Redis、RabbitMQ 等連線資訊放在設定檔，不耦合程式。
   - 測試環境可用輕量替代（如 testcontainers 啟動 DB/Redis）。

5. Build, Release, Run（明確分離建置、發佈、執行）

原則：建置（build）、發佈（release）、執行（run）必須分開，避免環境污染。
解決方案：
   - CI Pipeline：
   - Build：Maven package + 前端 npm build → Docker image
   - Release：將 image 標記版本，儲存於 GitLab Container Registry
   - Run：在目標環境（K8s/VM）部署指定版本

6. Processes（應用程式以一個或多個 stateless process 執行）

原則：應用程式應該是無狀態的，狀態應存放在 DB 或 Cache。
解決方案：
   - Spring Boot 無狀態設計，不在 JVM session 中存放狀態。
   - 使用 Redis 儲存 session（如果需要 session clustering）。

7. Port binding（服務自給自足，透過 port 對外提供服務）

原則：應用程式必須能自己啟動 HTTP server，而不是依賴外部 web server。
解決方案：
   - Spring Boot 內建 Tomcat/Netty → 直接透過 server.port 綁定。
   - Vue3 前端 → 透過 nginx or vite dev server 提供服務。

8. Concurrency（透過進程模型擴展應用程式）

原則：應用程式應能透過啟動多個 process 來擴充。
解決方案：
   - Spring Boot 後端：可水平擴展多個容器，透過 Kubernetes HPA / Docker swarm。
   - 前端：使用 CDN + 負載平衡 部署。

9. Disposability（快速啟動與優雅關閉）
原則：應用程式應快速啟動，並能安全終止。
解決方案：
   - Spring Boot 啟動快（數秒內）。
   - 使用 K8s readiness/liveness probe 檢查服務。
   - 使用 Spring Boot graceful shutdown 支援優雅關閉。

10. Dev/prod parity（開發、測試、正式環境保持一致）

原則：盡量讓開發環境接近正式環境。
解決方案：
   - 開發、測試、正式環境統一使用 Docker + K8s。
   - DB schema 同步，使用 Flyway/Liquibase 管理版本。
   - 使用 GitLab CI/CD pipeline 保持一致流程。

11. Logs（將 log 當成事件流）

原則：應用程式不應管理 log 檔案，應將 log 輸出到 stdout/stderr。
解決方案：
   - Spring Boot：使用 Logback 輸出到 console。
   - 前端：使用 Sentry 或 Elastic APM 收集 log。
   - Log 收集：ELK (Elasticsearch + Logstash + Kibana) 或 Loki + Grafana。

12. Admin processes（管理工作當作一次性任務執行）

原則：資料庫 migration 或 batch job 應獨立於應用程式主進程。
解決方案：
   - DB migration：使用 Flyway/Liquibase 自動化。
   - 批次任務：使用 Spring Batch / Quartz，透過 CI/CD 或 K8s CronJob 執行。

✅ 總結建議

- 程式碼管理：GitLab 單一 repo + 分支策略
- 建置與執行：Maven + Docker + GitLab CI/CD
- 設定管理：環境變數 + Secret Manager
-部署架構：Kubernetes + 負載平衡 + Redis session
- 觀測性：ELK/Loki + Prometheus + Grafana
- 自動化：Flyway 管理 DB schema，GitLab pipeline 控制 release 流程