+++
date = '2026-01-30T19:39:44+08:00'
draft = false
title = 'Kubernetes教學手冊'
tags = ['教學', '工具', 'Kubernetes', '容器編排平台', 'Gateway API']
categories = ['教學']
+++

# Kubernetes教學手冊

| 項目 | 內容 |
| --- | --- |
| **文件版本** | 2.0（企業標準技術白皮書版） |
| **最後更新** | 2026-10-01 |
| **版本基準** | Kubernetes **v1.37.1**（主線，所有範例的基準）；1.34／1.35 的差異以 `📌 1.34／1.35 差異` 標示 |
| **周邊元件基準** | containerd 2.4.1、etcd 3.7（kubeadm 預設）、Gateway API v1.6.2、Helm 4.3.0、Cilium 1.20.2／Calico 3.32.2、Prometheus 3.15、Argo CD 3.5 |
| **適用對象** | 後端工程師、DevOps／SRE、平台工程師、系統架構師、資安人員 |
| **定位** | 企業內部 Kubernetes 標準教材與導入參考 |
| **文件維護** | 內部技術團隊（Created by Eric Cheng） |

> 🆕 **v2.0 改版重點**
>
> - **版本基準從 1.29 改為 1.37.1**：1.29 已於 2025-02-28 EOL。本版依 Kubernetes 1.37.1 原始碼與官方文件逐章查證，並註記 1.34／1.35 的差異。
> - **重大生態系變化**：Ingress NGINX 已於 2026-03-24 退役（第 4 章並列 Ingress 與 Gateway API，並提供遷移指南）；cgroup v1 自 1.35 起預設拒絕啟動、1.36 起必須 containerd 2.x（第 2、11 章）；Bitnami 免費映像下架、Helm 4 發布（第 12 章）。
> - **修正 v1.0 的錯誤與過時內容**：共 41 項，完整清單見[附錄 D.2](#d2-v10--v20-更正對照表)。
> - **新增章節**：第 8 章「安全強化」、第 15 章「疑難排解手冊」、第 16 章「1.29 → 1.37 版本演進」，以及附錄 B–F。
> - 每章結尾新增「💡 本章實務建議」；新增段落標示 🆕，更正段落標示 ⚠️。

## 閱讀指引

| 讀者角色 | 建議閱讀順序 | 重點章節 |
| --- | --- | --- |
| 初次接觸 Kubernetes 的工程師 | 1 → 3 → 4 → 5 → 7 | [1.3 核心物件概念](#13-核心物件概念)、[3.3 Deployment 與 ReplicaSet](#33-deployment-與-replicaset) |
| 後端／應用開發者 | 3 → 5 → 6 → 13 → 14 | [6.2 Health Check](#62-health-checklivenessreadinessstartup-probe)、[13.5 優雅關機](#135-spring-boot-優雅關機與零停機發版) |
| 平台／SRE 工程師 | 2 → 9 → 10 → 11 → 15 | [10.2 etcd 備份與還原](#102-etcd-備份與還原)、[11.4 破壞性變更檢查](#114-棄用-api-與破壞性變更檢查) |
| 系統架構師 | 1 → 4 → 10.1 → 14 → 16 | [4.7 Gateway API](#47-gateway-apiv16)、[14.3 企業環境實務建議](#143-企業環境實務建議) |
| 資安人員 | 8 → 4.9 → 12.3 → 14.3 | [8.5 Admission 控制](#85-admission-控制validatingmutatingadmissionpolicy-與政策引擎)、[8.10 供應鏈安全](#810-供應鏈安全) |
| 從舊版升級的團隊 | 16 → 11 → 4.8 | [16.3 建議升級路徑](#163-從-129-升級到-137-的建議路徑)、[4.8 Ingress NGINX 遷移](#48-從-ingress-nginx-遷移到-gateway-api) |

> 📌 **標示說明**：🆕 v2.0 新增；⚠️ v2.0 更正或重要警示；📌 補充說明與版本差異；✅ 建議做法。功能成熟度標示為「x.y GA／Beta／Alpha」，以 Kubernetes 官方 feature gate 文件為準。

## 目錄

<!-- TOC-AUTO-BEGIN -->

- [1. Kubernetes 系統架構](#1-kubernetes-系統架構)
  - [1.1 Kubernetes 核心設計理念](#11-kubernetes-核心設計理念)
    - [1.1.1 宣告式配置（Declarative Configuration）](#111-宣告式配置declarative-configuration)
    - [1.1.2 控制迴圈（Control Loop）與調和（Reconciliation）](#112-控制迴圈control-loop與調和reconciliation)
    - [1.1.3 鬆耦合與可擴展性](#113-鬆耦合與可擴展性)
  - [1.2 Cluster 架構說明](#12-cluster-架構說明)
    - [1.2.1 整體架構圖](#121-整體架構圖)
    - [1.2.2 Control Plane 元件說明](#122-control-plane-元件說明)
    - [1.2.3 Worker Node 元件說明](#123-worker-node-元件說明)
    - [1.2.4 一個 Pod 從建立到執行的流程](#124-一個-pod-從建立到執行的流程)
    - [1.2.5 實務注意事項：etcd 是叢集的「心臟」](#125-實務注意事項etcd-是叢集的心臟)
  - [1.3 核心物件概念](#13-核心物件概念)
    - [1.3.1 物件模型：apiVersion／kind／metadata／spec／status](#131-物件模型apiversionkindmetadataspecstatus)
    - [1.3.2 Pod](#132-pod)
    - [1.3.3 Node](#133-node)
    - [1.3.4 Namespace](#134-namespace)
    - [1.3.5 Label、Selector 與建議標籤](#135-labelselector-與建議標籤)
    - [1.3.6 Annotation](#136-annotation)
    - [1.3.7 OwnerReference、Finalizer 與垃圾回收](#137-ownerreferencefinalizer-與垃圾回收)
  - [1.4 Kubernetes 與傳統部署差異](#14-kubernetes-與傳統部署差異)
    - [1.4.1 導入效益參考（實務案例）](#141-導入效益參考實務案例)
    - [1.4.2 什麼情況「不」適合導入 Kubernetes](#142-什麼情況不適合導入-kubernetes)
  - [1.5 API 版本與功能成熟度](#15-api-版本與功能成熟度)
    - [1.5.1 Feature Gate 與成熟度階段](#151-feature-gate-與成熟度階段)
    - [1.5.2 API 棄用政策重點](#152-api-棄用政策重點)
    - [1.5.3 本手冊使用的 API 版本對照](#153-本手冊使用的-api-版本對照)
  - [1.6 💡 本章實務建議](#16--本章實務建議)
- [2. Kubernetes 安裝與環境建置](#2-kubernetes-安裝與環境建置)
  - [2.1 常見安裝方式比較](#21-常見安裝方式比較)
    - [2.1.1 kubeadm 安裝（Ubuntu 24.04／Debian 12，Kubernetes v1.37）](#211-kubeadm-安裝ubuntu-2404debian-12kubernetes-v137)
    - [2.1.2 以設定檔初始化 Control Plane（建議做法）](#212-以設定檔初始化-control-plane建議做法)
    - [2.1.3 Managed Kubernetes 比較](#213-managed-kubernetes-比較)
    - [2.1.4 本地開發環境（kind）](#214-本地開發環境kind)
  - [2.2 基本環境需求](#22-基本環境需求)
    - [2.2.1 硬體需求](#221-硬體需求)
    - [2.2.2 作業系統需求](#222-作業系統需求)
    - [2.2.3 網路需求（連接埠）](#223-網路需求連接埠)
  - [2.3 Cluster 初始化流程](#23-cluster-初始化流程)
    - [2.3.1 Container Runtime 安裝（containerd 2.x）](#231-container-runtime-安裝containerd-2x)
    - [2.3.2 高可用 Control Plane](#232-高可用-control-plane)
    - [2.3.3 CNI 選型與安裝](#233-cni-選型與安裝)
  - [2.4 安裝後驗證](#24-安裝後驗證)
    - [2.4.1 常見安裝問題排查](#241-常見安裝問題排查)
  - [2.5 💡 本章實務建議](#25--本章實務建議)
- [3. 工作負載資源](#3-工作負載資源)
  - [3.1 工作負載資源總覽](#31-工作負載資源總覽)
  - [3.2 Pod 生命週期](#32-pod-生命週期)
    - [3.2.1 Pod Phase](#321-pod-phase)
    - [3.2.2 Pod Conditions](#322-pod-conditions)
    - [3.2.3 Pod 終止流程（Graceful Shutdown）](#323-pod-終止流程graceful-shutdown)
  - [3.3 Deployment 與 ReplicaSet](#33-deployment-與-replicaset)
    - [3.3.1 Deployment 完整範例（企業標準範本）](#331-deployment-完整範例企業標準範本)
    - [3.3.2 Deployment、ReplicaSet 與 Pod 的關係](#332-deploymentreplicaset-與-pod-的關係)
  - [3.4 StatefulSet](#34-statefulset)
  - [3.5 DaemonSet、Job 與 CronJob](#35-daemonsetjob-與-cronjob)
    - [3.5.1 DaemonSet](#351-daemonset)
    - [3.5.2 Job（含失敗政策）](#352-job含失敗政策)
    - [3.5.3 CronJob](#353-cronjob)
  - [3.6 Init 容器與 Sidecar 容器](#36-init-容器與-sidecar-容器)
    - [3.6.1 容器層級重啟規則（1.35 Beta）](#361-容器層級重啟規則135-beta)
  - [3.7 💡 本章實務建議](#37--本章實務建議)
- [4. 服務網路與流量入口](#4-服務網路與流量入口)
  - [4.1 Kubernetes 網路模型](#41-kubernetes-網路模型)
  - [4.2 Service 類型](#42-service-類型)
    - [4.2.1 Service YAML 範例](#421-service-yaml-範例)
    - [4.2.2 trafficDistribution 與流量政策](#422-trafficdistribution-與流量政策)
    - [4.2.3 已棄用：Service externalIPs](#423-已棄用service-externalips)
  - [4.3 EndpointSlice](#43-endpointslice)
  - [4.4 kube-proxy 模式](#44-kube-proxy-模式)
  - [4.5 CoreDNS 與服務探索](#45-coredns-與服務探索)
  - [4.6 Ingress 與 Ingress Controller](#46-ingress-與-ingress-controller)
    - [4.6.1 Ingress 架構](#461-ingress-架構)
    - [4.6.2 Ingress NGINX 退役說明（重要）](#462-ingress-nginx-退役說明重要)
    - [4.6.3 仍在維護的 Ingress Controller 比較（2026-09）](#463-仍在維護的-ingress-controller-比較2026-09)
    - [4.6.4 Ingress 設定範例（F5 NGINX Ingress Controller）](#464-ingress-設定範例f5-nginx-ingress-controller)
    - [4.6.5 pathType 說明](#465-pathtype-說明)
  - [4.7 Gateway API（v1.6）](#47-gateway-apiv16)
    - [4.7.1 角色導向的資源模型](#471-角色導向的資源模型)
    - [4.7.2 安裝 Gateway API CRD 與實作（以 Envoy Gateway 為例）](#472-安裝-gateway-api-crd-與實作以-envoy-gateway-為例)
    - [4.7.3 Gateway 與 HTTPRoute 範例](#473-gateway-與-httproute-範例)
    - [4.7.4 金絲雀發布（權重分流）與標頭路由](#474-金絲雀發布權重分流與標頭路由)
    - [4.7.5 GRPCRoute、TLSRoute 與 TCPRoute](#475-grpcroutetlsroute-與-tcproute)
    - [4.7.6 跨 Namespace 參照：ReferenceGrant](#476-跨-namespace-參照referencegrant)
    - [4.7.7 Gateway API 實作選型](#477-gateway-api-實作選型)
    - [4.7.8 Ingress 與 Gateway API 比較](#478-ingress-與-gateway-api-比較)
  - [4.8 從 Ingress NGINX 遷移到 Gateway API](#48-從-ingress-nginx-遷移到-gateway-api)
    - [4.8.1 遷移流程](#481-遷移流程)
    - [4.8.2 使用 ingress2gateway](#482-使用-ingress2gateway)
    - [4.8.3 常見 annotation 對照表](#483-常見-annotation-對照表)
  - [4.9 NetworkPolicy 基礎](#49-networkpolicy-基礎)
  - [4.10 💡 本章實務建議](#410--本章實務建議)
- [5. 設定與儲存管理](#5-設定與儲存管理)
  - [5.1 ConfigMap](#51-configmap)
    - [5.1.1 ConfigMap 定義與四種使用方式](#511-configmap-定義與四種使用方式)
    - [5.1.2 Immutable ConfigMap／Secret](#512-immutable-configmapsecret)
    - [5.1.3 從檔案載入環境變數（1.35 Beta）](#513-從檔案載入環境變數135-beta)
  - [5.2 Secret](#52-secret)
    - [5.2.1 Secret 類型與定義](#521-secret-類型與定義)
    - [5.2.2 Secret 安全建議](#522-secret-安全建議)
  - [5.3 Volume 類型總覽](#53-volume-類型總覽)
    - [5.3.1 Image Volume（1.36 GA）](#531-image-volume136-ga)
  - [5.4 PersistentVolume、PVC 與 StorageClass](#54-persistentvolumepvc-與-storageclass)
    - [5.4.1 動態佈建架構](#541-動態佈建架構)
    - [5.4.2 StorageClass 與 PVC 範例](#542-storageclass-與-pvc-範例)
    - [5.4.3 存取模式與回收策略](#543-存取模式與回收策略)
    - [5.4.4 線上擴容與失敗復原](#544-線上擴容與失敗復原)
    - [5.4.5 VolumeAttributesClass（1.34 GA）](#545-volumeattributesclass134-ga)
    - [5.4.6 找出閒置的 PVC（1.37 Beta）](#546-找出閒置的-pvc137-beta)
  - [5.5 VolumeSnapshot 與 VolumeGroupSnapshot](#55-volumesnapshot-與-volumegroupsnapshot)
  - [5.6 💡 本章實務建議](#56--本章實務建議)
- [6. 資源管理、排程與自動擴縮](#6-資源管理排程與自動擴縮)
  - [6.1 Resource Request / Limit 與 QoS](#61-resource-request--limit-與-qos)
    - [6.1.1 Request 與 Limit 的意義](#611-request-與-limit-的意義)
    - [6.1.2 CPU 與 Memory 單位](#612-cpu-與-memory-單位)
    - [6.1.3 QoS 等級與 CPU limit 的取捨](#613-qos-等級與-cpu-limit-的取捨)
    - [6.1.4 資源設定建議](#614-資源設定建議)
    - [6.1.5 Pod 層級資源（1.34 Beta）](#615-pod-層級資源134-beta)
    - [6.1.6 原地調整 Pod 資源（In-place Resize，1.35 GA）](#616-原地調整-pod-資源in-place-resize135-ga)
  - [6.2 Health Check：Liveness／Readiness／Startup Probe](#62-health-checklivenessreadinessstartup-probe)
    - [6.2.1 三種 Probe 比較](#621-三種-probe-比較)
    - [6.2.2 Probe 方式](#622-probe-方式)
    - [6.2.3 常見 Probe 設定錯誤](#623-常見-probe-設定錯誤)
  - [6.3 排程控制](#63-排程控制)
    - [6.3.1 排程機制總覽](#631-排程機制總覽)
    - [6.3.2 Node Affinity 與 Taints](#632-node-affinity-與-taints)
    - [6.3.3 PriorityClass 與搶占](#633-priorityclass-與搶占)
    - [6.3.4 Pod Disruption Budget（PDB）](#634-pod-disruption-budgetpdb)
  - [6.4 自動擴縮](#64-自動擴縮)
    - [6.4.1 HPA（autoscaling/v2）](#641-hpaautoscalingv2)
    - [6.4.2 HPA 縮到 0（1.37 Beta）](#642-hpa-縮到-0137-beta)
    - [6.4.3 KEDA 事件驅動擴展](#643-keda-事件驅動擴展)
    - [6.4.4 VPA](#644-vpa)
    - [6.4.5 Node 自動擴縮：Cluster Autoscaler 與 Karpenter](#645-node-自動擴縮cluster-autoscaler-與-karpenter)
  - [6.5 Dynamic Resource Allocation（DRA）概覽](#65-dynamic-resource-allocationdra概覽)
  - [6.6 💡 本章實務建議](#66--本章實務建議)
- [7. kubectl 與日常操作](#7-kubectl-與日常操作)
  - [7.1 kubectl 常用指令](#71-kubectl-常用指令)
    - [7.1.1 基本指令速查表](#711-基本指令速查表)
    - [7.1.2 輸出格式](#712-輸出格式)
    - [7.1.3 Server-Side Apply（SSA）](#713-server-side-applyssa)
  - [7.2 kubectl 使用者偏好：.kuberc（1.34 Beta）](#72-kubectl-使用者偏好kuberc134-beta)
  - [7.3 kubectl debug 與臨時容器](#73-kubectl-debug-與臨時容器)
  - [7.4 Deployment 發佈流程](#74-deployment-發佈流程)
  - [7.5 滾動更新與回滾](#75-滾動更新與回滾)
    - [7.5.1 滾動更新參數](#751-滾動更新參數)
    - [7.5.2 回滾](#752-回滾)
  - [7.6 進階發布策略：藍綠與金絲雀](#76-進階發布策略藍綠與金絲雀)
    - [7.6.1 以 Service selector 實作藍綠部署](#761-以-service-selector-實作藍綠部署)
    - [7.6.2 以 Argo Rollouts 自動化金絲雀](#762-以-argo-rollouts-自動化金絲雀)
  - [7.7 kubectl 外掛與輔助工具](#77-kubectl-外掛與輔助工具)
  - [7.8 💡 本章實務建議](#78--本章實務建議)
- [8. 安全強化](#8-安全強化)
  - [8.1 認證（Authentication）](#81-認證authentication)
    - [8.1.1 認證方式比較](#811-認證方式比較)
    - [8.1.2 結構化認證設定（Structured Authentication Configuration，1.34 GA）](#812-結構化認證設定structured-authentication-configuration134-ga)
  - [8.2 RBAC 權限控管](#82-rbac-權限控管)
    - [8.2.1 RBAC 架構](#821-rbac-架構)
    - [8.2.2 RBAC 設定範例](#822-rbac-設定範例)
    - [8.2.3 高風險權限清單](#823-高風險權限清單)
    - [8.2.4 1.34–1.37 的授權改進](#824-134137-的授權改進)
  - [8.3 ServiceAccount 與 Token 安全](#83-serviceaccount-與-token-安全)
  - [8.4 Pod Security Admission 與 securityContext](#84-pod-security-admission-與-securitycontext)
    - [8.4.1 Pod Security Standards 三個等級](#841-pod-security-standards-三個等級)
    - [8.4.2 符合 restricted 的 securityContext 範本](#842-符合-restricted-的-securitycontext-範本)
    - [8.4.3 User Namespaces（1.36 GA）](#843-user-namespaces136-ga)
  - [8.5 Admission 控制：Validating／MutatingAdmissionPolicy 與政策引擎](#85-admission-控制validatingmutatingadmissionpolicy-與政策引擎)
    - [8.5.1 ValidatingAdmissionPolicy 範例：禁止 latest 標籤、要求資源設定](#851-validatingadmissionpolicy-範例禁止-latest-標籤要求資源設定)
    - [8.5.2 MutatingAdmissionPolicy 範例：自動補上預設標籤](#852-mutatingadmissionpolicy-範例自動補上預設標籤)
  - [8.6 Secret 靜態加密：KMS v2](#86-secret-靜態加密kms-v2)
  - [8.7 工作負載身分：Pod 憑證與 ClusterTrustBundle（1.37 GA）](#87-工作負載身分pod-憑證與-clustertrustbundle137-ga)
  - [8.8 網路安全進階：零信任與 Service Mesh](#88-網路安全進階零信任與-service-mesh)
  - [8.9 Audit Log（稽核日誌）](#89-audit-log稽核日誌)
  - [8.10 供應鏈安全](#810-供應鏈安全)
  - [8.11 合規基準與安全檢查](#811-合規基準與安全檢查)
  - [8.12 💡 本章實務建議](#812--本章實務建議)
- [9. 可觀測性：監控、日誌與追蹤](#9-可觀測性監控日誌與追蹤)
  - [9.1 可觀測性架構總覽](#91-可觀測性架構總覽)
  - [9.2 Prometheus 3 與 kube-prometheus-stack](#92-prometheus-3-與-kube-prometheus-stack)
    - [9.2.1 資源指標：metrics-server 與 metrics.k8s.io（1.37 GA）](#921-資源指標metrics-server-與-metricsk8sio137-ga)
    - [9.2.2 安裝 kube-prometheus-stack](#922-安裝-kube-prometheus-stack)
    - [9.2.3 以 ServiceMonitor 收集應用指標](#923-以-servicemonitor-收集應用指標)
    - [9.2.4 Kubernetes 必看指標與告警](#924-kubernetes-必看指標與告警)
  - [9.3 日誌收集](#93-日誌收集)
    - [9.3.1 日誌收集架構](#931-日誌收集架構)
    - [9.3.2 Fluent Bit 部署（Helm）](#932-fluent-bit-部署helm)
    - [9.3.3 應用程式日誌建議（結構化 JSON）](#933-應用程式日誌建議結構化-json)
    - [9.3.4 Node 日誌輪替](#934-node-日誌輪替)
  - [9.4 分散式追蹤與 OpenTelemetry](#94-分散式追蹤與-opentelemetry)
  - [9.5 Kubernetes Events](#95-kubernetes-events)
  - [9.6 管理介面：Headlamp](#96-管理介面headlamp)
  - [9.7 💡 本章實務建議](#97--本章實務建議)
- [10. 維運與管理](#10-維運與管理)
  - [10.1 Namespace 與多團隊隔離](#101-namespace-與多團隊隔離)
    - [10.1.1 多租戶模型選擇](#1011-多租戶模型選擇)
    - [10.1.2 Namespace 設計策略](#1012-namespace-設計策略)
    - [10.1.3 Namespace 範本：Quota 與 LimitRange](#1013-namespace-範本quota-與-limitrange)
  - [10.2 etcd 備份與還原](#102-etcd-備份與還原)
    - [10.2.1 備份](#1021-備份)
    - [10.2.2 還原（kubeadm stacked etcd，單一成員示意）](#1022-還原kubeadm-stacked-etcd單一成員示意)
  - [10.3 憑證管理](#103-憑證管理)
    - [10.3.1 kubeadm 叢集的憑證](#1031-kubeadm-叢集的憑證)
    - [10.3.2 應用層憑證（cert-manager）](#1032-應用層憑證cert-manager)
  - [10.4 Cluster 容量與資源管理](#104-cluster-容量與資源管理)
    - [10.4.1 容量觀察指令](#1041-容量觀察指令)
    - [10.4.2 Node 資源保留](#1042-node-資源保留)
    - [10.4.3 容量規劃建議](#1043-容量規劃建議)
  - [10.5 災難復原與 Velero](#105-災難復原與-velero)
    - [10.5.1 DR 策略分級](#1051-dr-策略分級)
    - [10.5.2 Velero 備份](#1052-velero-備份)
  - [10.6 常見營運風險與因應](#106-常見營運風險與因應)
  - [10.7 💡 本章實務建議](#107--本章實務建議)
- [11. 升級策略](#11-升級策略)
  - [11.1 版本與支援政策](#111-版本與支援政策)
  - [11.2 Version Skew 政策（元件版本差距）](#112-version-skew-政策元件版本差距)
  - [11.3 升級順序](#113-升級順序)
  - [11.4 棄用 API 與破壞性變更檢查](#114-棄用-api-與破壞性變更檢查)
    - [11.4.1 檢查棄用 API](#1141-檢查棄用-api)
    - [11.4.2 1.34 → 1.37 逐版破壞性變更與注意事項](#1142-134--137-逐版破壞性變更與注意事項)
  - [11.5 kubeadm 升級流程](#115-kubeadm-升級流程)
    - [11.5.1 第一台 Control Plane](#1151-第一台-control-plane)
    - [11.5.2 其他 Control Plane](#1152-其他-control-plane)
    - [11.5.3 Worker Node（分批進行）](#1153-worker-node分批進行)
  - [11.6 Managed Kubernetes 升級](#116-managed-kubernetes-升級)
  - [11.7 應用程式升級注意事項](#117-應用程式升級注意事項)
  - [11.8 升級前檢查清單](#118-升級前檢查清單)
  - [11.9 💡 本章實務建議](#119--本章實務建議)
- [12. CI/CD 與 GitOps](#12-cicd-與-gitops)
  - [12.1 CI/CD 整體流程](#121-cicd-整體流程)
  - [12.2 GitLab CI 範例](#122-gitlab-ci-範例)
  - [12.3 容器映像管理策略](#123-容器映像管理策略)
    - [12.3.1 映像命名規範](#1231-映像命名規範)
    - [12.3.2 映像標籤策略](#1232-映像標籤策略)
    - [12.3.3 Registry 治理](#1233-registry-治理)
  - [12.4 Helm 4](#124-helm-4)
    - [12.4.1 Helm 4 相對 Helm 3 的主要變化](#1241-helm-4-相對-helm-3-的主要變化)
    - [12.4.2 Chart 結構](#1242-chart-結構)
    - [12.4.3 Helm 常用指令](#1243-helm-常用指令)
    - [12.4.4 values.yaml 範例](#1244-valuesyaml-範例)
  - [12.5 Kustomize](#125-kustomize)
  - [12.6 GitOps：Argo CD 與 Flux](#126-gitopsargo-cd-與-flux)
  - [12.7 環境晉升（Promotion）](#127-環境晉升promotion)
  - [12.8 💡 本章實務建議](#128--本章實務建議)
- [13. 應用系統整合](#13-應用系統整合)
  - [13.1 外部資料庫與既有系統](#131-外部資料庫與既有系統)
    - [13.1.1 方式一：ExternalName（外部有 DNS 名稱）](#1311-方式一externalname外部有-dns-名稱)
    - [13.1.2 方式二：無 selector 的 Service + EndpointSlice（外部只有 IP）](#1312-方式二無-selector-的-service--endpointslice外部只有-ip)
    - [13.1.3 連線治理](#1313-連線治理)
  - [13.2 Prometheus 整合](#132-prometheus-整合)
  - [13.3 External Secrets Operator 與 Vault](#133-external-secrets-operator-與-vault)
  - [13.4 cert-manager 憑證自動化](#134-cert-manager-憑證自動化)
  - [13.5 Spring Boot 優雅關機與零停機發版](#135-spring-boot-優雅關機與零停機發版)
    - [13.5.1 Kubernetes 端設定](#1351-kubernetes-端設定)
    - [13.5.2 Spring Boot 端設定](#1352-spring-boot-端設定)
  - [13.6 💡 本章實務建議](#136--本章實務建議)
- [14. 最佳實踐與常見反模式](#14-最佳實踐與常見反模式)
  - [14.1 建議遵循的設計原則](#141-建議遵循的設計原則)
    - [14.1.1 最佳實踐清單](#1411-最佳實踐清單)
    - [14.1.2 企業標準工作負載範本（整合範例）](#1412-企業標準工作負載範本整合範例)
  - [14.2 常見錯誤與踩雷經驗](#142-常見錯誤與踩雷經驗)
    - [14.2.1 常見反模式](#1421-常見反模式)
    - [14.2.2 實際踩雷案例](#1422-實際踩雷案例)
  - [14.3 企業環境實務建議](#143-企業環境實務建議)
    - [14.3.1 金融業特殊考量](#1431-金融業特殊考量)
    - [14.3.2 法規與控制對照（參考）](#1432-法規與控制對照參考)
    - [14.3.3 平台工程（Platform Engineering）建議](#1433-平台工程platform-engineering建議)
  - [14.4 💡 本章實務建議](#144--本章實務建議)
- [15. 疑難排解手冊](#15-疑難排解手冊)
  - [15.1 故障排查總流程](#151-故障排查總流程)
  - [15.2 Pod 停在 Pending](#152-pod-停在-pending)
  - [15.3 CrashLoopBackOff（反覆重啟）](#153-crashloopbackoff反覆重啟)
  - [15.4 ImagePullBackOff／ErrImagePull](#154-imagepullbackofferrimagepull)
  - [15.5 OOMKilled 與記憶體問題](#155-oomkilled-與記憶體問題)
  - [15.6 網路與 Service 問題](#156-網路與-service-問題)
  - [15.7 DNS 問題](#157-dns-問題)
  - [15.8 儲存與 Volume 問題](#158-儲存與-volume-問題)
  - [15.9 Node NotReady](#159-node-notready)
  - [15.10 Control Plane 與憑證問題](#1510-control-plane-與憑證問題)
  - [15.11 💡 本章實務建議](#1511--本章實務建議)
- [16. Kubernetes 1.29 → 1.37 版本演進](#16-kubernetes-129--137-版本演進)
  - [16.1 各版本重點總覽](#161-各版本重點總覽)
  - [16.2 依主題整理的演進](#162-依主題整理的演進)
    - [16.2.1 工作負載](#1621-工作負載)
    - [16.2.2 網路](#1622-網路)
    - [16.2.3 Node 與 Runtime](#1623-node-與-runtime)
    - [16.2.4 安全](#1624-安全)
    - [16.2.5 儲存](#1625-儲存)
    - [16.2.6 自動擴縮與排程](#1626-自動擴縮與排程)
    - [16.2.7 工具與可觀測性](#1627-工具與可觀測性)
  - [16.3 從 1.29 升級到 1.37 的建議路徑](#163-從-129-升級到-137-的建議路徑)
  - [16.4 💡 本章實務建議](#164--本章實務建議)
- [附錄 A：檢查清單（Checklist）](#附錄-a檢查清單checklist)
  - [A.1 新服務部署檢查清單](#a1-新服務部署檢查清單)
  - [A.2 日常維運檢查清單](#a2-日常維運檢查清單)
  - [A.3 升級前檢查清單](#a3-升級前檢查清單)
  - [A.4 安全基準檢查清單](#a4-安全基準檢查清單)
- [附錄 B：常見問答（Q&A）](#附錄-b常見問答qa)
- [附錄 C：常用指令速查](#附錄-c常用指令速查)
  - [C.1 叢集與 Node](#c1-叢集與-node)
  - [C.2 工作負載](#c2-工作負載)
  - [C.3 除錯](#c3-除錯)
  - [C.4 網路與 Gateway](#c4-網路與-gateway)
  - [C.5 etcd](#c5-etcd)
- [附錄 D：版本紀錄](#附錄-d版本紀錄)
  - [D.1 文件版本歷史](#d1-文件版本歷史)
  - [D.2 v1.0 → v2.0 更正對照表](#d2-v10--v20-更正對照表)
  - [D.3 v2.0 新增章節](#d3-v20-新增章節)
- [附錄 E：查證紀錄](#附錄-e查證紀錄)
  - [E.1 待確認項目](#e1-待確認項目)
- [附錄 F：參考資料](#附錄-f參考資料)
  - [F.1 官方文件與原始碼](#f1-官方文件與原始碼)
  - [F.2 網路與流量](#f2-網路與流量)
  - [F.3 安全](#f3-安全)
  - [F.4 維運、可觀測性與交付](#f4-維運可觀測性與交付)
  - [F.5 書籍](#f5-書籍)

<!-- TOC-AUTO-END -->

---

## 1. Kubernetes 系統架構

### 1.1 Kubernetes 核心設計理念

Kubernetes（簡稱 K8s）源自 Google 內部的 Borg 系統，2014 年開源，2016 年成為 CNCF 第一個託管專案，2018 年最早從 CNCF 畢業。它的核心價值是：**把「要跑什麼」和「怎麼跑」分開**。使用者用宣告式 API 描述期望狀態，平台自己負責排程、修復、擴縮和網路連通。

#### 1.1.1 宣告式配置（Declarative Configuration）

- **核心概念**：使用者描述「期望狀態」（Desired State），Kubernetes 把實際狀態（Actual State）持續收斂到期望狀態。
- **優點**：設定可以版本控制、可以重複套用（冪等）、方便審計，也能銜接 GitOps。
- **和命令式的差別**：`kubectl create`／`kubectl scale` 是命令式；`kubectl apply -f`（Server-Side Apply 更好）是宣告式。正式環境應以宣告式為主。

```yaml
# 宣告式範例：期望狀態是 3 個 nginx Pod
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app.kubernetes.io/name: nginx
spec:
  replicas: 3            # 期望狀態：3 個副本
  selector:
    matchLabels:
      app.kubernetes.io/name: nginx
  template:
    metadata:
      labels:
        app.kubernetes.io/name: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.30.5   # 固定版本，不使用 latest
          ports:
            - containerPort: 80
```

#### 1.1.2 控制迴圈（Control Loop）與調和（Reconciliation）

每個控制器（Controller）都在做同一件事：**觀察 → 比較 → 行動**，週而復始。控制器透過 API Server 的 watch 機制取得變化，不會直接去碰其他元件。

```mermaid
flowchart LR
    A["觀察 Observe<br/>watch API Server"] --> B["比較 Diff<br/>spec vs status"]
    B --> C["行動 Act<br/>建立/刪除/更新物件"]
    C --> A
```

| 概念 | 說明 |
| --- | --- |
| `spec` | 使用者宣告的期望狀態 |
| `status` | 控制器回報的實際狀態 |
| `metadata.generation` ／ `status.observedGeneration` | 判斷控制器是否已處理最新的 spec；1.35 起 Pod 也會回報 `observedGeneration`（GA） |
| Level-triggered | 控制器依「目前狀態」而不是「事件」行動，漏掉事件也能自我修正 |

#### 1.1.3 鬆耦合與可擴展性

- **API 驅動**：所有元件（包括 kubectl、控制器、kubelet）都只和 API Server 溝通，etcd 只有 API Server 能存取。
- **標準化插件介面**：
  - **CRI**（Container Runtime Interface）：containerd、CRI-O。
  - **CNI**（Container Network Interface）：Cilium、Calico、Flannel 等。
  - **CSI**（Container Storage Interface）：各家儲存廠商的驅動程式。
- **擴充 API**：CRD（Custom Resource Definition）＋ Operator 模式、Aggregated API、Admission Webhook／Admission Policy。
- **Kubernetes Patterns**：O'Reilly《Kubernetes Patterns》把常見做法整理為五大類，本手冊各章會對應：

| 類別 | 代表模式 | 本手冊章節 |
| --- | --- | --- |
| 基礎模式（Foundational） | Predictable Demands、Declarative Deployment、Health Probe、Managed Lifecycle、Automated Placement | 3、6 |
| 行為模式（Behavioral） | Batch Job、Periodic Job、Daemon Service、Singleton Service、Stateful Service、Service Discovery | 3、4 |
| 結構模式（Structural） | Init Container、Sidecar、Adapter、Ambassador | 3.6 |
| 設定模式（Configuration） | EnvVar Configuration、Configuration Resource、Immutable Configuration | 5 |
| 進階模式（Advanced） | Controller、Operator、Elastic Scale、Image Builder | 6、12 |

---

### 1.2 Cluster 架構說明

#### 1.2.1 整體架構圖

```mermaid
flowchart TB
    subgraph CP["Control Plane（控制平面）"]
        API["kube-apiserver"]
        ETCD[("etcd")]
        SCHED["kube-scheduler"]
        KCM["kube-controller-manager"]
        CCM["cloud-controller-manager<br/>（選用）"]
    end

    subgraph W1["Worker Node 1"]
        K1["kubelet"]
        KP1["kube-proxy<br/>（或 eBPF CNI 取代）"]
        CR1["containerd / CRI-O"]
        P1["Pod"]
        P2["Pod"]
    end

    subgraph W2["Worker Node 2"]
        K2["kubelet"]
        KP2["kube-proxy"]
        CR2["containerd / CRI-O"]
        P3["Pod"]
    end

    API <--> ETCD
    SCHED --> API
    KCM --> API
    CCM --> API
    K1 --> API
    K2 --> API
    KP1 --> API
    KP2 --> API
    K1 --> CR1
    K2 --> CR2
    CR1 --> P1
    CR1 --> P2
    CR2 --> P3
```

> 📌 **重點**：箭頭方向代表「誰主動連誰」。除了 `kubectl exec/logs/port-forward` 以及 API Server 呼叫 Webhook 之外，幾乎都是元件主動連到 API Server，API Server 不會主動推送指令給 kubelet。

#### 1.2.2 Control Plane 元件說明

| 元件 | 功能 | 高可用做法 |
| --- | --- | --- |
| **kube-apiserver** | 唯一的 API 入口：認證 → 授權 → Admission → 驗證 → 寫入 etcd；提供 watch | 無狀態，多副本，前面放 L4 負載平衡器 |
| **etcd** | 強一致性（Raft）的鍵值儲存，存放所有叢集狀態 | 3 或 5 個成員（奇數），跨故障域 |
| **kube-scheduler** | 依資源、親和性、拓撲、污點等為 Pod 選擇 Node | 多副本 + Leader Election |
| **kube-controller-manager** | 執行內建控制器（Deployment、ReplicaSet、Node、Job、EndpointSlice、ServiceAccount 等） | 多副本 + Leader Election |
| **cloud-controller-manager** | 和雲端 API 整合（LoadBalancer、Node 生命週期、路由） | 由雲端供應商提供 |

> 🆕 **v2.0 新增（1.34–1.37 Control Plane 改進）**
>
> - **Watch cache 韌性初始化**（1.34 GA）：API Server 重啟時，watch cache 尚未就緒的請求會改為直接讀 etcd 或回傳可重試的錯誤，不會整批卡住。
> - **Streaming list**（1.34 GA）：大型 list 請求改為串流回應，API Server 記憶體尖峰大幅下降。
> - **Snapshottable API server cache**（1.34 Beta）：分頁 list 可以直接從 cache 提供一致的快照。
> - **Mixed version proxy**（1.36 Beta）：多個 API Server 版本混合時（升級期間），請求會被代理到能處理該資源版本的 API Server，避免 404。
> - **Storage Version Migrator**（1.37 GA）：內建的儲存版本遷移，不需要另外安裝 kube-storage-version-migrator。

#### 1.2.3 Worker Node 元件說明

| 元件 | 功能 | 說明 |
| --- | --- | --- |
| **kubelet** | Node 代理程式：向 API Server 註冊 Node、依 PodSpec 啟動容器、執行 Probe、回報狀態 | 每個 Node 必須有；不是容器，由 systemd 管理 |
| **kube-proxy** | 依 Service／EndpointSlice 設定封包轉送規則 | 1.33 起 `nftables` 模式 GA；`ipvs` 模式自 1.35 起棄用；Cilium 等 eBPF CNI 可以完全取代 kube-proxy |
| **Container Runtime** | 透過 CRI 拉映像、建立容器 | containerd 2.x 或 CRI-O；1.36 起不再支援 containerd 1.x |
| **CNI Plugin** | 配置 Pod 網路、IP、NetworkPolicy | 通常以 DaemonSet 部署 |
| **CoreDNS** | 叢集內 DNS（嚴格說是附加元件，以 Deployment 部署） | kube-dns 自 1.37 起棄用 |

> ⚠️ **v2.0 更正**：v1.0 說「kube-proxy 每個 Node 必須有」。實際上它是可替換的元件，使用 Cilium kube-proxy replacement 等方案時可以不部署。

#### 1.2.4 一個 Pod 從建立到執行的流程

```mermaid
sequenceDiagram
    participant U as 使用者 / CI
    participant A as kube-apiserver
    participant E as etcd
    participant C as Deployment / ReplicaSet Controller
    participant S as kube-scheduler
    participant K as kubelet
    participant R as containerd
    U->>A: kubectl apply（Deployment）
    A->>A: 認證、授權、Admission、驗證
    A->>E: 寫入 Deployment
    C->>A: watch 到 Deployment，建立 ReplicaSet 與 Pod
    S->>A: watch 到未排程 Pod，寫入 spec.nodeName
    K->>A: watch 到分配給自己的 Pod
    K->>R: CRI：拉映像、建立 Sandbox 與容器
    K->>A: 回報 Pod status（Running / Ready）
```

#### 1.2.5 實務注意事項：etcd 是叢集的「心臟」

etcd 存放所有叢集資料（含 Secret），**一定要定期備份並演練還原**，詳細流程見 [10.2 etcd 備份與還原](#102-etcd-備份與還原)。

```bash
# etcd 3.4 起 etcdctl 預設就是 v3 API，不需要再設定 ETCDCTL_API=3
sudo etcdctl snapshot save /backup/etcd-$(date +%Y%m%d-%H%M).db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# 檢查快照（etcd 3.6 起只能用 etcdutl，etcdctl snapshot status 已移除）
sudo etcdutl snapshot status /backup/etcd-20261001-0200.db -w table
```

> ⚠️ **v2.0 更正**：v1.0 的備份指令前面加了 `ETCDCTL_API=3`。etcd 3.4 起這是預設值，不需要設定。etcd 3.6 已移除 `etcdctl snapshot restore/status`，要改用 `etcdutl`。kubeadm 1.37 預設部署 etcd **3.7.0**。

---

### 1.3 核心物件概念

#### 1.3.1 物件模型：apiVersion／kind／metadata／spec／status

每個 Kubernetes 物件都有相同的骨架：

| 欄位 | 說明 | 範例 |
| --- | --- | --- |
| `apiVersion` | API 群組／版本 | `v1`（core）、`apps/v1`、`networking.k8s.io/v1`、`gateway.networking.k8s.io/v1` |
| `kind` | 資源種類 | `Pod`、`Deployment`、`HTTPRoute` |
| `metadata` | 名稱、命名空間、標籤、註解、ownerReferences、finalizers | — |
| `spec` | 期望狀態 | — |
| `status` | 實際狀態（由控制器寫入，使用者不應修改） | — |

#### 1.3.2 Pod

- Kubernetes **最小的排程與部署單位**，同一 Pod 內的容器共享網路命名空間（同一個 IP、可用 `localhost` 互通）與 Volume。
- Pod 是「可拋棄」的：重建後 IP 會變，因此對外一律透過 Service 存取。
- 一個 Pod 可以包含：主容器、**Init 容器**、**Sidecar 容器**（1.33 GA 的原生 sidecar，以 `restartPolicy: Always` 的 init 容器實作，詳見 [3.6 Init 容器與 Sidecar 容器](#36-init-容器與-sidecar-容器)）、臨時除錯容器（Ephemeral Container）。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-log-sidecar
  labels:
    app.kubernetes.io/name: myapp
spec:
  initContainers:
    # 原生 Sidecar：比主容器先啟動、比主容器晚結束
    - name: log-shipper
      image: fluent/fluent-bit:5.1.2
      restartPolicy: Always
      volumeMounts:
        - name: shared-logs
          mountPath: /var/log/app
  containers:
    - name: main-app
      image: registry.example.com/myapp:1.4.2
      ports:
        - containerPort: 8080
      volumeMounts:
        - name: shared-logs
          mountPath: /var/log/app
  volumes:
    - name: shared-logs
      emptyDir: {}
```

> ⚠️ **v2.0 更正**：v1.0 的多容器範例把 sidecar 寫在 `containers` 裡，而且用 `fluentd:latest`。這樣 Job 類工作負載會因為 sidecar 不結束而無法完成，也無法保證啟動順序。1.33 起建議改用原生 sidecar，並固定映像版本。

#### 1.3.3 Node

- 實際執行 Pod 的機器（VM 或實體機），由 kubelet 向 API Server 註冊。
- Node 物件包含容量（capacity）、可分配量（allocatable）、狀況（conditions）、污點（taints）。

```bash
# 查看所有 Node（含 IP、OS、核心、Runtime 版本）
kubectl get nodes -o wide

# 查看 Node 詳細資訊（Conditions、Allocatable、已分配資源）
kubectl describe node <node-name>

# 標記 Node 不可排程（維護前）
kubectl cordon <node-name>

# 驅逐 Node 上的 Pod（會遵守 PodDisruptionBudget）
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data --timeout=10m

# 維護完成後恢復排程
kubectl uncordon <node-name>

# 1.36 GA：直接查詢 Node 上的系統日誌（需在 kubelet 設定 enableSystemLogHandler 與 enableSystemLogQuery）
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/logs/?query=kubelet&tailLines=100"
```

#### 1.3.4 Namespace

- 叢集內的**邏輯隔離邊界**：名稱範圍、RBAC、ResourceQuota、LimitRange、NetworkPolicy、Pod Security Admission 都以 Namespace 為單位。
- Namespace **不是**安全邊界的全部：Node、PV、ClusterRole、CRD 等是叢集範圍資源。強隔離需求請參考 [10.1 多團隊隔離](#101-namespace-與多團隊隔離)。
- 1.34 起刪除 Namespace 時會依序刪除資源（Ordered Namespace Deletion GA），先刪 Pod 再刪 NetworkPolicy 等，避免刪除過程中出現「Pod 還在但防護規則已不見」的空窗。

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: order-prod
  labels:
    environment: production
    team: order
    # Pod Security Admission：強制 restricted 等級（詳見第 8 章）
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
```

#### 1.3.5 Label、Selector 與建議標籤

- **Label**：附加在物件上的鍵值對，用於**識別與篩選**（Service、Deployment、NetworkPolicy 都靠它選擇 Pod）。
- **Selector**：等值（`app=web`）或集合（`env in (prod,staging)`）篩選。
- Deployment 的 `spec.selector` 建立後**不可修改**，設計時要只放穩定的標籤（不要放版本號）。

官方建議使用 `app.kubernetes.io/*` 前綴的 **Recommended Labels**，Helm、Argo CD、監控工具都能直接辨識：

```yaml
metadata:
  labels:
    app.kubernetes.io/name: order-service        # 應用名稱
    app.kubernetes.io/instance: order-service-prod
    app.kubernetes.io/version: "1.4.2"           # 版本（只放 metadata，不放 selector）
    app.kubernetes.io/component: api             # 元件角色
    app.kubernetes.io/part-of: ecommerce         # 所屬系統
    app.kubernetes.io/managed-by: helm           # 管理工具
    # 企業自訂標籤（建議加公司網域前綴）
    example.com/team: order
    example.com/cost-center: "CC-1024"
```

> ⚠️ **v2.0 更正**：v1.0 建議使用 `version`、`tier` 等自訂標籤，並把 `version` 放進 selector。版本標籤放進 selector 會讓每次發版都必須重建 Deployment。本版改用官方建議標籤，版本只放在 metadata。

#### 1.3.6 Annotation

- 存放**非識別用途**的中繼資料，值可以很長，不能用來篩選。
- 常見用途：工具設定（Ingress Controller、Prometheus）、變更紀錄、聯絡人資訊。

```yaml
metadata:
  annotations:
    kubernetes.io/change-cause: "Release 1.4.2: fix order rounding (CHG-20261001-01)"
    example.com/owner: "order-team@example.com"
    example.com/runbook: "https://wiki.example.com/runbooks/order-service"
```

> 📌 `deployment.kubernetes.io/revision` 是控制器自動維護的註解，不要手動設定（v1.0 範例手動寫入，已移除）。

#### 1.3.7 OwnerReference、Finalizer 與垃圾回收

- **ownerReferences**：Deployment → ReplicaSet → Pod 的從屬關係，刪除擁有者時會級聯刪除（`--cascade=background|foreground|orphan`）。
- **finalizers**：刪除前必須完成的清理工作（例如 PVC 的 `kubernetes.io/pvc-protection`）。物件「卡在 Terminating」通常是 finalizer 沒有被移除，**先查清楚是哪個控制器負責**，不要直接清空 finalizer。

---

### 1.4 Kubernetes 與傳統部署差異

| 面向 | 傳統 VM／單機部署 | Kubernetes |
| --- | --- | --- |
| **部署單位** | VM 或實體機 | 容器（Pod） |
| **擴展方式** | 手動增加機器 | HPA／VPA／KEDA 自動擴縮，Cluster Autoscaler／Karpenter 自動增減 Node |
| **高可用** | 需自行設計（Keepalived、叢集軟體） | 內建自癒：重啟、重新排程、滾動更新 |
| **服務發現** | 固定 IP、DNS、硬體負載平衡器 | Service + CoreDNS + EndpointSlice |
| **流量入口** | 硬體 LB／反向代理 | Gateway API／Ingress + Controller |
| **配置管理** | 設定檔散落各台機器 | ConfigMap／Secret 集中管理、GitOps |
| **版本回滾** | 複雜且風險高 | `kubectl rollout undo`、Helm rollback、Argo CD 回到前一個 commit |
| **資源利用** | 偏低（每個 VM 都有 OS 開銷） | 偏高（容器共用 Kernel、bin packing） |
| **維運重點** | 主機與 OS | 平台（叢集生命週期、版本升級、多租戶治理） |

```mermaid
flowchart LR
    subgraph T["傳統部署"]
        VM1["VM 1<br/>App A"]
        VM2["VM 2<br/>App B"]
        VM3["VM 3<br/>App A"]
    end

    subgraph K["Kubernetes 部署"]
        N1["Node 1"] --> PA1["Pod A"]
        N1 --> PB1["Pod B"]
        N2["Node 2"] --> PA2["Pod A"]
        N2 --> PB2["Pod B"]
        N2 --> PA3["Pod A"]
    end
```

#### 1.4.1 導入效益參考（實務案例）

**某金融系統導入 Kubernetes 前後對比**（內部案例，數字僅供參考，會因組織成熟度而有很大差異）：

| 指標 | 導入前 | 導入後 |
| --- | --- | --- |
| 部署時間 | 2–4 小時（人工、夜間窗口） | 5–10 分鐘（CI/CD、白天滾動） |
| 資源利用率 | 30–40% | 55–70% |
| 故障恢復時間 | 30 分鐘以上 | 1–3 分鐘（自動重啟／重新排程） |
| 環境一致性 | 經常有差異 | 映像不可變、設定版本化 |

#### 1.4.2 什麼情況「不」適合導入 Kubernetes

- 應用數量很少（只有 1–3 個服務），團隊也沒有平台維運能力：用 PaaS 或 VM 更划算。
- 強烈依賴特定硬體或授權綁定主機的商用軟體。
- 團隊尚未具備容器化、CI/CD、可觀測性的基礎：先補足基礎，再上 Kubernetes。

---

### 1.5 API 版本與功能成熟度

#### 1.5.1 Feature Gate 與成熟度階段

| 階段 | 預設 | 說明 | 正式環境建議 |
| --- | --- | --- | --- |
| **Alpha** | 關閉 | 可能有 bug、隨時移除、不保證相容 | 不要使用 |
| **Beta** | 新的 Beta API 預設關閉；Beta 功能多數預設開啟 | 功能大致完整，細節仍可能改變 | 評估後可用，需追蹤變更 |
| **GA（Stable）** | 開啟 | 長期支援，Feature Gate 之後會被鎖定並移除 | 可放心使用 |

> 📌 **1.24 起的政策**：新的 Beta **API**（例如 `v1beta1` 的新資源）預設不啟用，必須明確開啟。

#### 1.5.2 API 棄用政策重點

- GA API（`v1`）不會在同一個主版本內被移除。
- Beta API 棄用後至少保留 9 個月或 3 個版本（取較長者）。
- 使用棄用 API 時，API Server 會回傳 `Warning:` 標頭，kubectl 會直接顯示；也可以從 `apiserver_requested_deprecated_apis` 指標找出仍在使用的用戶端（詳見 [11.4 棄用 API 檢查](#114-棄用-api-與破壞性變更檢查)）。

#### 1.5.3 本手冊使用的 API 版本對照

| 資源 | 正式環境建議的 apiVersion | 備註 |
| --- | --- | --- |
| Deployment／StatefulSet／DaemonSet | `apps/v1` | — |
| Job／CronJob | `batch/v1` | — |
| Ingress／NetworkPolicy | `networking.k8s.io/v1` | — |
| EndpointSlice | `discovery.k8s.io/v1` | `v1` Endpoints 自 1.33 起棄用 |
| HPA | `autoscaling/v2` | — |
| PodDisruptionBudget | `policy/v1` | — |
| ValidatingAdmissionPolicy | `admissionregistration.k8s.io/v1` | 1.30 GA |
| MutatingAdmissionPolicy | `admissionregistration.k8s.io/v1` | 1.36 GA |
| Gateway API（Gateway／HTTPRoute／GRPCRoute／ReferenceGrant／TCPRoute／UDPRoute） | `gateway.networking.k8s.io/v1` | 需安裝 CRD（v1.6.2） |
| kubeadm 設定 | `kubeadm.k8s.io/v1beta4` | kubeadm 1.37 原始碼已有 `v1`，但仍以 v1beta4 為優先版本 |

---

### 1.6 💡 本章實務建議

1. **以宣告式 + GitOps 為唯一變更途徑**：正式環境禁止手動 `kubectl edit`，所有變更走 Git → CI → Argo CD／Flux。
2. **etcd 備份是 Day 1 工作**：每日至少一次快照、異地保存、每季還原演練。
3. **統一使用 `app.kubernetes.io/*` 建議標籤**，並訂出企業自訂標籤規範（團隊、成本中心、資料等級）。
4. **追蹤 Feature Gate 成熟度**：只在正式環境使用 GA 功能；Beta 功能要列入風險清單。
5. **不要把 kube-proxy 模式當成理所當然**：新叢集優先評估 `nftables` 或 eBPF（Cilium），避免使用已棄用的 `ipvs`。

---

## 2. Kubernetes 安裝與環境建置

### 2.1 常見安裝方式比較

| 安裝方式 | 適用場景 | 複雜度 | 維運負擔 | 備註 |
| --- | --- | --- | --- | --- |
| **kubeadm** | 地端／私有雲自建、學習原理 | 中 | 高 | 官方工具，只負責 bootstrap，不管 OS 與 LB |
| **Managed K8s**（GKE／EKS／AKS） | 公有雲 | 低 | 低 | Control Plane 由雲端代管 |
| **RKE2 ／ k3s** | 地端企業（RKE2 符合 CIS）、邊緣（k3s） | 低–中 | 中 | SUSE Rancher 生態 |
| **OpenShift ／ OKD** | 需要商業支援與整合平台的企業 | 高 | 中 | 內建 Router、Registry、OperatorHub |
| **Cluster API（CAPI）** | 以宣告式管理大量叢集的生命週期 | 高 | 中 | 叢集本身也是 Kubernetes 物件 |
| **kind** | 本機開發、CI 整合測試 | 低 | 無 | 以容器模擬 Node |
| **minikube** | 本機學習 | 低 | 無 | 內建多種 addon |

> 📌 **選型原則**：能用 Managed 就用 Managed；必須自建時，正式環境優先考慮有商業支援的發行版（OpenShift、RKE2、VMware、Rancher 等）或 Cluster API，kubeadm 適合有足夠平台團隊的組織。

#### 2.1.1 kubeadm 安裝（Ubuntu 24.04／Debian 12，Kubernetes v1.37）

以下步驟在**所有節點**執行（Control Plane 與 Worker）。Container Runtime 的安裝見 [2.3.1](#231-container-runtime-安裝containerd-2x)。

```bash
# 0. 前置：關閉或設定 swap（見 2.2.2）、載入核心參數
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
EOF
sudo sysctl --system

# 1. 安裝前置套件
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg

# 2. 新增 Kubernetes apt repository（pkgs.k8s.io 以 minor 版本分 repo）
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.37/deb/Release.key \
  | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.37/deb/ /' \
  | sudo tee /etc/apt/sources.list.d/kubernetes.list

# 3. 安裝 kubelet、kubeadm、kubectl，並鎖定版本避免被一般 apt upgrade 升級
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
sudo systemctl enable --now kubelet
```

RHEL 9／Rocky 9 等使用 dnf 的發行版：

```bash
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.37/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.37/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
EOF
sudo dnf install -y kubelet kubeadm kubectl --setopt=disable_excludes=kubernetes
sudo systemctl enable --now kubelet
```

> ⚠️ **v2.0 更正**：v1.0 的 repo 路徑寫 `v1.29`，而 1.29 已於 2025-02-28 EOL。pkgs.k8s.io 每個 minor 版本是獨立的 repo，**升級 minor 版本時必須先修改 repo 路徑**（見 [11.5 kubeadm 升級流程](#115-kubeadm-升級流程)）。舊的 `apt.kubernetes.io`／`yum.kubernetes.io` 已在 2024 年停用。

#### 2.1.2 以設定檔初始化 Control Plane（建議做法）

正式環境不要只靠命令列參數，請用 kubeadm 設定檔（`kubeadm.k8s.io/v1beta4`）並納入版本控制：

```yaml
# kubeadm-config.yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: InitConfiguration
nodeRegistration:
  criSocket: unix:///run/containerd/containerd.sock
  kubeletExtraArgs:
    - name: node-ip
      value: "10.10.0.11"
---
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: v1.37.1
clusterName: prod-tpe-01
controlPlaneEndpoint: "k8s-api.example.internal:6443"   # HA 時指向 VIP／LB
networking:
  podSubnet: 10.244.0.0/16
  serviceSubnet: 10.96.0.0/12
  dnsDomain: cluster.local
apiServer:
  certSANs:
    - k8s-api.example.internal
    - 10.10.0.10
  extraArgs:
    - name: audit-log-path
      value: /var/log/kubernetes/audit/audit.log
    - name: audit-policy-file
      value: /etc/kubernetes/audit-policy.yaml
  extraVolumes:
    - name: audit-policy
      hostPath: /etc/kubernetes/audit-policy.yaml
      mountPath: /etc/kubernetes/audit-policy.yaml
      readOnly: true
      pathType: File
    - name: audit-log
      hostPath: /var/log/kubernetes/audit
      mountPath: /var/log/kubernetes/audit
      pathType: DirectoryOrCreate
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
cgroupDriver: systemd          # containerd 2.x 支援時，kubelet 會改從 CRI 取得
serverTLSBootstrap: true       # kubelet 服務憑證走 CSR，需另行核准（見 10.3）
---
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: nftables                 # 1.33 GA；未設定時 Linux 預設仍是 iptables
```

```bash
# 預先拉映像（離線環境可搭配私有 Registry：imageRepository）
sudo kubeadm config images pull --config kubeadm-config.yaml

# 初始化第一個 Control Plane，--upload-certs 讓其他 Control Plane 可以加入
sudo kubeadm init --config kubeadm-config.yaml --upload-certs

# 設定 kubectl（admin.conf 是超級管理員憑證，正式環境請改用 OIDC，見 8.1）
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Worker 加入（token 預設 24 小時有效，可用下列指令重新產生）
sudo kubeadm token create --print-join-command
sudo kubeadm join k8s-api.example.internal:6443 --token <token> \
  --discovery-token-ca-cert-hash sha256:<hash>
```

> 📌 **kubeadm 1.37 預設元件版本**（原始碼 `cmd/kubeadm/app/constants`）：etcd **3.7.0**、CoreDNS **v1.14.6**、pause **3.10.2**。kubeadm 1.37 支援的 kubelet 最低版本是 1.34（skew 3 個 minor）。
>
> 📌 **1.34／1.35 差異**：kubeadm `v1beta4` 自 1.31 起提供，1.34／1.35 都可以使用相同設定檔，只要調整 `kubernetesVersion`。`v1beta3` 仍可讀取，但建議用 `kubeadm config migrate` 轉換。

#### 2.1.3 Managed Kubernetes 比較

| 雲端服務 | 特色 | 全代管模式 | 計費重點（請以官方最新價格為準） |
| --- | --- | --- | --- |
| **GKE**（Google） | 最早的代管服務，升級與自動修復成熟；Release Channel（Rapid／Regular／Stable／Extended） | **Autopilot**：連 Node 都代管，以 Pod 資源計費 | 每叢集管理費（有免費額度）；Extended channel 另計 |
| **EKS**（AWS） | 和 IAM、VPC CNI、ALB 深度整合；EKS Pod Identity | **EKS Auto Mode**：代管 Node、Karpenter、LB、儲存 | Control Plane 按小時計費；超過標準支援期進入 Extended Support，費率較高 |
| **AKS**（Azure） | 和 Entra ID、Azure Policy 整合 | **AKS Automatic** | Free tier 不收 Control Plane 費但沒有 SLA；Standard／Premium tier 收費（含 SLA、LTS） |

> ⚠️ **v2.0 更正**：v1.0 寫「AKS 免收 Control Plane 費用」。目前只有 Free tier 不收費，而且沒有財務性 SLA；正式環境通常使用收費的 Standard tier。三家雲端都有「延長支援」方案，版本落後太久會產生額外費用，升級規劃見第 11 章。

#### 2.1.4 本地開發環境（kind）

```bash
# 安裝 kind v0.33.0（也可用 brew install kind / choco install kind）
go install sigs.k8s.io/kind@v0.33.0

# 建立單節點叢集（預設映像 kindest/node:v1.37.0）
kind create cluster --name dev

# 多節點叢集 + 指定版本（建議連 digest 一起固定，避免映像被覆蓋）
cat <<EOF | kind create cluster --name dev-multi --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    image: kindest/node:v1.37.0
    extraPortMappings:
      - containerPort: 30080
        hostPort: 8080
  - role: worker
    image: kindest/node:v1.37.0
  - role: worker
    image: kindest/node:v1.37.0
networking:
  kubeProxyMode: nftables
EOF

# 把本機映像載入 kind（不用推到 Registry）
kind load docker-image myapp:dev --name dev-multi

# 刪除叢集
kind delete cluster --name dev-multi
```

> 📌 kind 只適合開發與 CI。要測 1.36 或 1.34 時，請在 kind release notes 找對應的 `kindest/node` 映像與 digest。

---

### 2.2 基本環境需求

#### 2.2.1 硬體需求

| 角色 | 最低需求（kubeadm 檢查） | 正式環境建議 |
| --- | --- | --- |
| Control Plane | 2 vCPU、2 GB RAM | 4–8 vCPU、16 GB RAM、**SSD／NVMe**（etcd 對磁碟延遲很敏感，WAL fsync p99 應小於 10ms） |
| Worker Node | 1 vCPU、2 GB RAM（實務上至少 2 vCPU） | 8–32 vCPU、32–128 GB RAM，依工作負載決定 |
| etcd（外部部署時） | — | 2–4 vCPU、8 GB RAM、獨立 SSD |

> 📌 **節點規模**：Kubernetes 官方測試上限是單一叢集 5,000 個 Node、150,000 個 Pod、每 Node 110 個 Pod（預設 `maxPods`）。企業實務上，單一叢集通常控制在數百個 Node 以內，用多叢集分散風險。

#### 2.2.2 作業系統需求

- **Linux 發行版**：Ubuntu 22.04／24.04、Debian 12、RHEL／Rocky／Alma 9、SLES 15 SP6+ 等，需使用 systemd。
- **cgroup v2（必要）**：1.35 起 kubelet 預設 `failCgroupV1: true`，在 cgroup v1 節點上**會直接拒絕啟動**。RHEL 8、CentOS 7、Ubuntu 20.04 等舊系統預設是 cgroup v1，必須升級 OS。
- **核心版本**：cgroup v2 建議 5.8 以上；kube-proxy `nftables` 模式需要 5.13 以上與 `nft` 1.0.1 以上；Pod User Namespaces 需要 6.3 以上。
- **Swap**：1.34 起 Node Swap 已 GA，但 kubelet 預設 `failSwapOn: true`。若不打算使用 swap，維持關閉即可；若要使用，請明確設定（見下方範例）。

```bash
# 確認 cgroup 版本：輸出 cgroup2fs 表示 cgroup v2
stat -fc %T /sys/fs/cgroup/

# 方案 A：不使用 swap（最單純）
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
```

```yaml
# 方案 B：允許 swap（1.34 GA），在 KubeletConfiguration 設定
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
failSwapOn: false
memorySwap:
  swapBehavior: LimitedSwap   # 只有 Burstable QoS 的 Pod 可以依記憶體 request 比例使用 swap
```

> ⚠️ **v2.0 更正**：v1.0 寫「必須停用 Swap」、「Kernel 4.15+」、「CentOS Stream 9+」。現在 swap 可以受控使用；核心需求取決於 cgroup v2 與 nftables；還必須確認是 cgroup v2，否則 1.35 以上的 kubelet 無法啟動。
>
> 📌 **1.34 差異**：1.34 的 kubelet 在 cgroup v1 上只會警告；升級到 1.35 之前，務必完成所有 Node 的 cgroup v2 遷移。緊急時可以暫時設定 `failCgroupV1: false`，但 cgroup v1 支援已排定在未來版本移除。

#### 2.2.3 網路需求（連接埠）

| 方向 | 連接埠 | 元件 | 用途 |
| --- | --- | --- | --- |
| Control Plane 入站 | 6443 | kube-apiserver | Kubernetes API（所有元件與使用者） |
| Control Plane 入站 | 2379–2380 | etcd | 用戶端／成員間通訊（只開給 Control Plane） |
| Control Plane 入站 | 10257 | kube-controller-manager | HTTPS 健康檢查與指標（本機） |
| Control Plane 入站 | 10259 | kube-scheduler | HTTPS 健康檢查與指標（本機） |
| 所有 Node 入站 | 10250 | kubelet | kubelet API（exec／logs／metrics） |
| 所有 Node 入站 | 10256 | kube-proxy | 健康檢查（LoadBalancer 使用） |
| Worker 入站 | 30000–32767 | NodePort | NodePort Service（可自訂範圍） |
| 依 CNI 而定 | 例如 4789/UDP（VXLAN）、8472/UDP（Flannel／Cilium VXLAN）、179/TCP（Calico BGP）、4240（Cilium health） | CNI | Pod 網路 |

**網段規劃**：Pod CIDR、Service CIDR、Node 網段、企業內網**不可重疊**。大型叢集建議 Pod CIDR 至少 /16。需要 IPv6 時，Kubernetes 支援雙堆疊（Dual-stack，1.23 GA）。

---

### 2.3 Cluster 初始化流程

```mermaid
flowchart TD
    A["準備 OS<br/>cgroup v2、時間同步、sysctl"] --> B["安裝 Container Runtime<br/>containerd 2.x / CRI-O"]
    B --> C["安裝 kubeadm / kubelet / kubectl"]
    C --> D["準備 API Server 端點<br/>LB 或 kube-vip"]
    D --> E["kubeadm init（設定檔）"]
    E --> F["安裝 CNI<br/>Cilium / Calico"]
    F --> G["加入其他 Control Plane"]
    G --> H["加入 Worker Node"]
    H --> I["安裝基礎元件<br/>metrics-server、Gateway、CSI、監控"]
    I --> J["驗證與基準測試"]
```

#### 2.3.1 Container Runtime 安裝（containerd 2.x）

Kubernetes 1.36 起**只支援 containerd 2.0 以上**。部分發行版內建的套件仍是 1.7 系列（安裝前請用 `apt-cache policy containerd` 或 `containerd --version` 確認），因此建議使用官方二進位檔，或發行版／Docker 套件庫提供的 2.x 套件。

```bash
# 1. 安裝 containerd 2.4.1（官方二進位檔）
CTRD=2.4.1
curl -LO https://github.com/containerd/containerd/releases/download/v${CTRD}/containerd-${CTRD}-linux-amd64.tar.gz
sudo tar Cxzvf /usr/local containerd-${CTRD}-linux-amd64.tar.gz
sudo curl -L -o /etc/systemd/system/containerd.service \
  https://raw.githubusercontent.com/containerd/containerd/main/containerd.service

# 2. 安裝 runc 與 CNI plugins
sudo install -m 755 runc.amd64 /usr/local/sbin/runc          # 從 opencontainers/runc v1.5.2 下載
sudo mkdir -p /opt/cni/bin
sudo tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.9.1.tgz

# 3. 產生預設設定（containerd 2.x 是 config version 3）
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml >/dev/null
```

containerd 2.x 的 systemd cgroup 設定路徑和 1.x **不同**：

```toml
# /etc/containerd/config.toml（containerd 2.x，version = 3）
version = 3

[plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc.options]
  SystemdCgroup = true

[plugins.'io.containerd.cri.v1.images']
  # 私有 Registry 鏡像設定建議放在 /etc/containerd/certs.d/<registry>/hosts.toml
  [plugins.'io.containerd.cri.v1.images'.registry]
    config_path = '/etc/containerd/certs.d'
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now containerd

# 驗證：crictl 需要指定 endpoint（或寫在 /etc/crictl.yaml）
sudo crictl --runtime-endpoint unix:///run/containerd/containerd.sock info | head -20
```

> ⚠️ **v2.0 更正**：v1.0 用 `apt-get install containerd` 加上 `sed 's/SystemdCgroup = false/SystemdCgroup = true/'`。這組做法只適用 containerd 1.x（config version 2，路徑是 `plugins."io.containerd.grpc.v1.cri"`），在 containerd 2.x 上不會生效，而 1.36 以上已不支援 1.x。可以觀察 kubelet 指標 `kubelet_cri_losing_support` 找出仍在使用舊 Runtime 的 Node。
>
> 📌 **cgroup driver 自動偵測**：1.34 起 `KubeletCgroupDriverFromCRI` 已 GA，kubelet 會向 containerd 2.x／CRI-O 詢問 cgroup driver，`KubeletConfiguration.cgroupDriver` 只在 Runtime 不支援時才作為後備。

#### 2.3.2 高可用 Control Plane

```mermaid
flowchart TB
    U["kubectl / Node / CI"] --> VIP["API VIP<br/>k8s-api.example.internal:6443<br/>（F5 / HAProxy / kube-vip）"]
    VIP --> CP1["Control Plane 1<br/>apiserver + etcd"]
    VIP --> CP2["Control Plane 2<br/>apiserver + etcd"]
    VIP --> CP3["Control Plane 3<br/>apiserver + etcd"]
    CP1 <--> CP2
    CP2 <--> CP3
    CP1 <--> CP3
```

| 拓撲 | 說明 | 優點 | 缺點 |
| --- | --- | --- | --- |
| **Stacked etcd**（kubeadm 預設） | etcd 和 Control Plane 同機 | 機器少、設定簡單 | Control Plane 故障同時影響 etcd 成員 |
| **External etcd** | etcd 獨立 3／5 台 | 故障域分離、可獨立調校 | 機器多、維運複雜 |

- Control Plane 數量用 **3 台**（容忍 1 台故障）或 **5 台**（容忍 2 台）；不要用偶數。
- 跨機房部署時，etcd 成員間 RTT 應低於 10ms；跨區域請改用多叢集。
- API VIP 可以用硬體 LB、HAProxy + Keepalived，或以 static Pod 部署的 **kube-vip**（v1.2.4）。

```bash
# 加入第 2、3 台 Control Plane（certificate-key 來自 kubeadm init --upload-certs 的輸出，2 小時有效）
sudo kubeadm join k8s-api.example.internal:6443 --token <token> \
  --discovery-token-ca-cert-hash sha256:<hash> \
  --control-plane --certificate-key <key>
```

#### 2.3.3 CNI 選型與安裝

| CNI | 版本（2026-09） | 特色 | 適用 |
| --- | --- | --- | --- |
| **Cilium** | 1.20.2 | eBPF、可取代 kube-proxy、L7 NetworkPolicy、Hubble 可觀測性、Gateway API 實作、Cluster Mesh | 新建叢集首選、需要可觀測性與進階政策 |
| **Calico** | 3.32.2 | BGP／VXLAN／eBPF 資料平面、成熟的 NetworkPolicy 與 GlobalNetworkPolicy | 地端資料中心、需與實體網路 BGP 互通 |
| **Flannel** | 0.28.9 | 簡單的 VXLAN overlay | 學習、測試；**不支援 NetworkPolicy** |
| 雲端原生 CNI | — | AWS VPC CNI、Azure CNI、GKE Dataplane V2（Cilium） | Managed K8s |

```bash
# 方案 A：Cilium（Helm），保留 kube-proxy
helm repo add cilium https://helm.cilium.io/
helm install cilium cilium/cilium --version 1.20.2 \
  --namespace kube-system \
  --set ipam.mode=kubernetes

# 方案 B：Calico（Tigera Operator）
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.32.2/manifests/tigera-operator.yaml
curl -LO https://raw.githubusercontent.com/projectcalico/calico/v3.32.2/manifests/custom-resources.yaml
# 修改 custom-resources.yaml 的 cidr 與 kubeadm podSubnet 一致後再套用
kubectl create -f custom-resources.yaml
```

> ⚠️ **v2.0 更正**：v1.0 以 Flannel `releases/latest` 作為範例。`latest` 讓安裝不可重現，而且 Flannel 不支援 NetworkPolicy，與第 8 章的安全要求衝突。本版改為 Cilium／Calico 並固定版本。

---

### 2.4 安裝後驗證

```bash
# 1. Node 狀態：全部 Ready，版本一致
kubectl get nodes -o wide

# 2. 系統 Pod：kube-system 全部 Running，沒有反覆重啟
kubectl get pods -n kube-system -o wide

# 3. 元件健康（取代已棄用的 kubectl get componentstatuses）
kubectl get --raw='/readyz?verbose'
kubectl get --raw='/livez?verbose'

# 4. 叢集與版本資訊
kubectl cluster-info
kubectl version

# 5. 部署測試應用並驗證 Service 與 DNS
kubectl create deployment nginx-test --image=nginx:1.30.5 --replicas=2
kubectl expose deployment nginx-test --port=80
kubectl run dns-test --rm -it --image=busybox:1.37 --restart=Never -- \
  sh -c 'nslookup nginx-test.default.svc.cluster.local && wget -qO- http://nginx-test | head -5'

# 6. 清理
kubectl delete deployment,svc nginx-test
```

**正式環境建議再加做**：

- **一致性測試**：用 [Sonobuoy](https://github.com/vmware-tanzu/sonobuoy) 或 Hydrophone 跑 CNCF Conformance。
- **安全基準**：用 kube-bench（v0.16.0）檢查 CIS Kubernetes Benchmark。
- **網路驗證**：Cilium 可用 `cilium connectivity test`。

#### 2.4.1 常見安裝問題排查

| 問題 | 可能原因 | 排查／解決 |
| --- | --- | --- |
| Node `NotReady` | CNI 未安裝或 CNI Pod 失敗 | `kubectl describe node` 看 `NetworkReady=false`；檢查 CNI DaemonSet |
| kubelet 無法啟動，日誌出現 cgroup v1 | 1.35+ 在 cgroup v1 主機上 | 升級 OS 為 cgroup v2；暫時設定 `failCgroupV1: false` |
| kubelet 無法啟動，日誌出現 swap | `failSwapOn: true` 但主機開著 swap | 關閉 swap，或設定 `failSwapOn: false` + `LimitedSwap` |
| `kubeadm init` preflight 失敗 | `ip_forward` 未開、埠被占用、CPU／RAM 不足 | 依錯誤訊息修正；不要用 `--ignore-preflight-errors=all` |
| Pod 一直 `ContainerCreating` | CNI 二進位檔或設定缺漏、Runtime 問題 | `journalctl -u kubelet`、`crictl ps -a`、`/etc/cni/net.d/` |
| 無法拉映像 | 防火牆、Proxy、私有 Registry 憑證 | 設定 containerd `certs.d`、HTTP(S)_PROXY 環境變數 |
| API Server 無法連線 | 防火牆擋 6443、憑證 SAN 不含 VIP | 開放 6443；`kubeadm init` 的 `certSANs` 要包含 VIP 和 DNS 名稱 |
| CoreDNS `CrashLoopBackOff` | 主機 `/etc/resolv.conf` 指向 127.0.0.53 造成迴圈 | kubelet 設定 `resolvConf: /run/systemd/resolve/resolv.conf` |

---

### 2.5 💡 本章實務建議

1. **新叢集一律 1.37 + containerd 2.x + cgroup v2**；舊 Node 先完成 OS 升級再升 Kubernetes。
2. **kubeadm 設定檔納入 Git**，包含 audit policy、certSANs、kube-proxy 模式等，確保可以重建。
3. **Control Plane 至少 3 台並使用 SSD**；API 端點使用 DNS 名稱，不要直接寫死 IP。
4. **CNI 選擇要考慮 NetworkPolicy 與可觀測性**；正式環境不要用 Flannel。
5. **所有元件固定版本**（Helm chart、manifest URL、映像 tag 甚至 digest），禁止 `latest`。
6. **Managed K8s 也要規劃升級**：避免進入雲端的延長支援收費期。

---

## 3. 工作負載資源

### 3.1 工作負載資源總覽

| 資源 | 用途 | 典型場景 | Pod 身分 |
| --- | --- | --- | --- |
| **Deployment** | 無狀態應用、滾動更新 | Web／API 服務 | 隨機名稱、可互換 |
| **ReplicaSet** | 維持副本數（由 Deployment 管理） | 不直接使用 | 同上 |
| **StatefulSet** | 有狀態應用，需要穩定名稱與獨立儲存 | 資料庫、Kafka、ZooKeeper、Elasticsearch | 固定序號 `name-0`、`name-1` |
| **DaemonSet** | 每個（或指定）Node 執行一份 | 日誌收集、監控 Agent、CNI、CSI Node | 每 Node 一個 |
| **Job** | 執行到成功為止的批次工作 | 資料轉檔、報表、資料庫遷移 | 完成後停止 |
| **CronJob** | 排程建立 Job | 每日對帳、清理作業 | 同 Job |

> 📌 **原則**：正式環境不要直接建立裸 Pod（沒有控制器管理），Node 故障時裸 Pod 不會被重建。

---

### 3.2 Pod 生命週期

#### 3.2.1 Pod Phase

```mermaid
stateDiagram-v2
    [*] --> Pending: 建立 Pod
    Pending --> Running: 已排程且至少一個容器啟動
    Pending --> Failed: 映像或設定錯誤導致無法啟動
    Running --> Succeeded: 所有容器成功結束（Job）
    Running --> Failed: 容器以非 0 結束且不再重啟
    Running --> Unknown: 與 Node 失聯
    Succeeded --> [*]
    Failed --> [*]
```

| Phase | 意義 | 常見原因 |
| --- | --- | --- |
| `Pending` | 已被 API Server 接受，但還沒全部容器建立 | 等待排程、拉映像、掛載 Volume |
| `Running` | 已綁定 Node，至少一個容器在執行 | — |
| `Succeeded` | 所有容器成功結束，不會重啟 | Job 完成 |
| `Failed` | 所有容器已結束，至少一個失敗 | 應用錯誤、OOMKilled 且 `restartPolicy: Never` |
| `Unknown` | 無法取得狀態 | Node 失聯 |

> ⚠️ **v2.0 更正**：`CrashLoopBackOff`、`ImagePullBackOff`、`OOMKilled` **不是** Phase，而是容器狀態（`state.waiting.reason`／`state.terminated.reason`），Pod Phase 通常仍是 `Running` 或 `Pending`。排查時要看 `kubectl describe pod` 的容器狀態。

#### 3.2.2 Pod Conditions

| Condition | 意義 |
| --- | --- |
| `PodScheduled` | 已排程到 Node |
| `PodReadyToStartContainers` | Sandbox 與網路已就緒，可以開始建立容器（1.37 GA） |
| `Initialized` | 所有 init 容器已成功完成（sidecar 已啟動） |
| `ContainersReady` | 所有容器都 Ready |
| `Ready` | Pod 可以接收流量（會被加入 EndpointSlice） |
| `DisruptionTarget` | Pod 即將因驅逐、搶占等原因被終止 |

#### 3.2.3 Pod 終止流程（Graceful Shutdown）

```mermaid
sequenceDiagram
    participant A as kube-apiserver
    participant K as kubelet
    participant E as EndpointSlice Controller
    participant C as 容器
    A->>A: 設定 deletionTimestamp（開始倒數 terminationGracePeriodSeconds）
    par 平行進行
        A->>E: Pod 進入 Terminating
        E->>E: 從 EndpointSlice 標記為 not ready
    and
        A->>K: kubelet watch 到刪除
        K->>C: 執行 preStop hook（例如 sleep 10）
        K->>C: 送出 SIGTERM
    end
    C->>C: 完成進行中的請求後結束
    K->>C: 逾時仍未結束則 SIGKILL
```

> 📌 **重點**：「從負載平衡移除」和「送 SIGTERM」是**平行**發生的，所以需要 `preStop` 稍微延遲，讓 kube-proxy／Gateway 有時間更新規則，詳見 [13.5 優雅關機](#135-spring-boot-優雅關機與零停機發版)。

---

### 3.3 Deployment 與 ReplicaSet

#### 3.3.1 Deployment 完整範例（企業標準範本）

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
  namespace: order-prod
  labels:
    app.kubernetes.io/name: order-service
    app.kubernetes.io/part-of: ecommerce
    app.kubernetes.io/version: "1.4.2"
  annotations:
    kubernetes.io/change-cause: "Release 1.4.2 (CHG-20261001-01)"
spec:
  replicas: 3
  revisionHistoryLimit: 10              # 保留可回滾的 ReplicaSet 數量
  progressDeadlineSeconds: 600          # 超過 10 分鐘沒有進展就標記失敗
  selector:
    matchLabels:
      app.kubernetes.io/name: order-service   # 只放穩定的標籤
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1                       # 更新時最多多出 1 個 Pod
      maxUnavailable: 0                 # 更新時不允許可用 Pod 減少
  template:
    metadata:
      labels:
        app.kubernetes.io/name: order-service
        app.kubernetes.io/version: "1.4.2"
    spec:
      serviceAccountName: order-service
      automountServiceAccountToken: false     # 應用不需要呼叫 K8s API 時關閉
      terminationGracePeriodSeconds: 60
      securityContext:
        runAsNonRoot: true
        runAsUser: 10001
        fsGroup: 10001
        seccompProfile:
          type: RuntimeDefault
      topologySpreadConstraints:              # 跨可用區、跨 Node 分散
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: ScheduleAnyway
          labelSelector:
            matchLabels:
              app.kubernetes.io/name: order-service
        - maxSkew: 1
          topologyKey: kubernetes.io/hostname
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              app.kubernetes.io/name: order-service
      containers:
        - name: order-service
          image: registry.example.com/ecommerce/order-service:1.4.2
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 8080
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: "production"
            - name: JAVA_TOOL_OPTIONS
              value: "-XX:MaxRAMPercentage=75.0"
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: order-db-credentials
                  key: password
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              memory: "1Gi"                   # 記憶體 limit = request；CPU 不設 limit（見 6.1）
          startupProbe:
            httpGet:
              path: /actuator/health/liveness
              port: http
            periodSeconds: 5
            failureThreshold: 36              # 最多等 180 秒啟動
          livenessProbe:
            httpGet:
              path: /actuator/health/liveness
              port: http
            periodSeconds: 10
            timeoutSeconds: 3
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /actuator/health/readiness
              port: http
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 3
          lifecycle:
            preStop:
              sleep:
                seconds: 10                   # 1.34 GA：不需要容器內有 sh
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          volumeMounts:
            - name: config
              mountPath: /app/config
              readOnly: true
            - name: tmp
              mountPath: /tmp
      volumes:
        - name: config
          configMap:
            name: order-service-config
        - name: tmp
          emptyDir:
            sizeLimit: 512Mi
```

> ⚠️ **v2.0 更正（相對 v1.0 範例）**：
>
> - 改用 `startupProbe` 取代很長的 `initialDelaySeconds`。
> - 加上 `securityContext`（restricted 等級）、`topologySpreadConstraints`、`preStop.sleep`、`progressDeadlineSeconds`。
> - selector 不再包含 `version` 標籤。
> - 移除 `prometheus.io/*` 註解：Prometheus Operator 改用 ServiceMonitor／PodMonitor（見 [9.2](#92-prometheus-3-與-kube-prometheus-stack)）。
> - CPU limit 改為不設定，避免 CFS throttling；理由見 [6.1](#61-resource-request--limit-與-qos)。

#### 3.3.2 Deployment、ReplicaSet 與 Pod 的關係

```mermaid
flowchart LR
    D["Deployment<br/>order-service"] --> RS1["ReplicaSet<br/>order-service-7d9f（rev 3，目前）"]
    D --> RS2["ReplicaSet<br/>order-service-5c4b（rev 2，replicas=0）"]
    RS1 --> P1["Pod"]
    RS1 --> P2["Pod"]
    RS1 --> P3["Pod"]
```

- 每次修改 `spec.template` 都會產生新的 ReplicaSet；舊 ReplicaSet 會縮到 0 並保留，作為回滾依據。
- 1.35 起 Deployment status 會顯示 **terminating replicas**（Beta），可以看出還有多少舊 Pod 正在結束。
- `kubectl rollout restart` 會修改 Pod template 註解，觸發重新滾動（常用於重新讀取 Secret）。

---

### 3.4 StatefulSet

StatefulSet 為每個 Pod 提供**穩定的網路身分**（`name-N.headless-svc`）與**獨立的 PVC**，並依序建立、更新、刪除。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres-headless
  namespace: data-prod
spec:
  clusterIP: None                 # Headless Service：DNS 直接回 Pod IP
  selector:
    app.kubernetes.io/name: postgres
  ports:
    - name: postgres
      port: 5432
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  namespace: data-prod
spec:
  serviceName: postgres-headless
  replicas: 3
  podManagementPolicy: OrderedReady   # 或 Parallel（彼此無依賴時加快啟動）
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 0                     # 調高可做分批（canary）更新
      maxUnavailable: 1                # 1.37 起預設可用（Beta）
  persistentVolumeClaimRetentionPolicy:
    whenDeleted: Retain                # 刪除 StatefulSet 時保留資料
    whenScaled: Retain
  selector:
    matchLabels:
      app.kubernetes.io/name: postgres
  template:
    metadata:
      labels:
        app.kubernetes.io/name: postgres
    spec:
      terminationGracePeriodSeconds: 120
      containers:
        - name: postgres
          image: postgres:18.6
          ports:
            - name: postgres
              containerPort: 5432
          resources:
            requests:
              cpu: "1"
              memory: 4Gi
            limits:
              memory: 4Gi
          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        storageClassName: fast-ssd
        resources:
          requests:
            storage: 100Gi
```

| 項目 | 說明 |
| --- | --- |
| Pod DNS | `postgres-0.postgres-headless.data-prod.svc.cluster.local` |
| PVC 名稱 | `data-postgres-0`、`data-postgres-1`… |
| `maxUnavailable` | 1.35 Beta；1.36 因 bug 暫時預設關閉；1.37 重新預設開啟 |
| `Recreate` 更新策略 | 1.37 Alpha（`StatefulSetRecreateStrategy`），正式環境先不要用 |

> 📌 **企業建議**：資料庫等關鍵狀態服務優先使用成熟的 **Operator**（例如 CloudNativePG、Strimzi、ECK），或直接使用雲端／既有的 DBA 管理平台。StatefulSet 只負責 Pod 與 PVC，不負責備份、主從切換、升級。

---

### 3.5 DaemonSet、Job 與 CronJob

#### 3.5.1 DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: node-exporter
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 10%        # 大型叢集可加快更新
  template:
    metadata:
      labels:
        app.kubernetes.io/name: node-exporter
    spec:
      hostNetwork: true
      hostPID: true
      priorityClassName: system-node-critical
      tolerations:
        - operator: Exists       # 包含 Control Plane 等有污點的 Node
      containers:
        - name: node-exporter
          image: quay.io/prometheus/node-exporter:v1.12.1
          args: ["--path.rootfs=/host"]
          resources:
            requests:
              cpu: 50m
              memory: 64Mi
            limits:
              memory: 128Mi
          volumeMounts:
            - name: root
              mountPath: /host
              readOnly: true
              mountPropagation: HostToContainer
      volumes:
        - name: root
          hostPath:
            path: /
```

> ⚠️ 使用 `hostNetwork`／`hostPID`／`hostPath` 的 DaemonSet 必須放在 Pod Security 為 `privileged` 的專用 Namespace（例如 `monitoring`），不要放在應用程式的 Namespace。

#### 3.5.2 Job（含失敗政策）

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: monthly-settlement
  namespace: batch-prod
spec:
  completions: 12                   # 12 個月份，各自處理
  parallelism: 4
  completionMode: Indexed           # 每個 Pod 取得 JOB_COMPLETION_INDEX
  backoffLimitPerIndex: 2           # 1.33 GA：每個 index 各自重試 2 次
  maxFailedIndexes: 3
  podReplacementPolicy: Failed      # 1.34 GA：舊 Pod 完全失敗後才建立替代 Pod
  activeDeadlineSeconds: 7200
  ttlSecondsAfterFinished: 86400    # 完成 1 天後自動清除
  podFailurePolicy:
    rules:
      - action: FailJob             # 程式回傳 42 代表資料錯誤，不要重試
        onExitCodes:
          containerName: settlement
          operator: In
          values: [42]
      - action: Ignore              # Node 驅逐、搶占造成的失敗不計入重試次數
        onPodConditions:
          - type: DisruptionTarget
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: settlement
          image: registry.example.com/batch/settlement:2.3.0
          args: ["--month-index=$(JOB_COMPLETION_INDEX)"]
          resources:
            requests:
              cpu: "1"
              memory: 2Gi
            limits:
              memory: 2Gi
```

| 欄位 | 成熟度 | 用途 |
| --- | --- | --- |
| `podFailurePolicy` | 1.31 GA | 依結束代碼或 Pod Condition 決定失敗、忽略或計數 |
| `backoffLimitPerIndex` | 1.33 GA | Indexed Job 每個 index 各自計算重試次數 |
| `successPolicy` | 1.33 GA | 指定哪些 index 成功即可視為整個 Job 成功（例如 leader 完成） |
| `podReplacementPolicy` | 1.34 GA | 避免新舊 Pod 同時存在（例如 GPU 不夠） |
| `managedBy` | 1.35 GA | 把 Job 交給外部控制器管理（例如 MultiKueue） |

#### 3.5.3 CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-report
  namespace: batch-prod
spec:
  schedule: "30 2 * * *"
  timeZone: "Asia/Taipei"           # 1.27 GA，不要再依賴 Control Plane 時區
  concurrencyPolicy: Forbid         # 前一次還沒結束就跳過
  startingDeadlineSeconds: 600
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 5
  jobTemplate:
    spec:
      backoffLimit: 2
      ttlSecondsAfterFinished: 172800
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: report
              image: registry.example.com/batch/daily-report:1.8.0
              resources:
                requests:
                  cpu: 200m
                  memory: 512Mi
                limits:
                  memory: 512Mi
```

> 📌 CronJob 不保證「剛好執行一次」：Control Plane 故障或時間跳動時可能漏跑或重複。業務邏輯必須**冪等**，重要排程應有補跑與告警機制。大量批次或需要佇列、配額管理時，可評估 **Kueue**。

---

### 3.6 Init 容器與 Sidecar 容器

| 類型 | 宣告位置 | 啟動時機 | 結束時機 | 典型用途 |
| --- | --- | --- | --- | --- |
| Init 容器 | `initContainers` | 依序執行，全部成功才啟動主容器 | 執行完畢即結束 | 等待相依服務、資料庫 schema 遷移、下載設定 |
| **原生 Sidecar**（1.33 GA） | `initContainers` + `restartPolicy: Always` | 依序啟動，**不必等它結束**就繼續 | 主容器結束後才停止 | 日誌轉送、Service Mesh Proxy、憑證更新 |
| 一般多容器 | `containers` | 同時啟動，無順序保證 | 各自獨立 | Adapter、Ambassador |

```yaml
spec:
  initContainers:
    - name: wait-for-db
      image: busybox:1.37
      command: ["sh", "-c", "until nc -z postgres-headless.data-prod 5432; do sleep 2; done"]
    - name: oauth-proxy                  # 原生 Sidecar
      image: quay.io/oauth2-proxy/oauth2-proxy:v7.15.4
      restartPolicy: Always
      ports:
        - containerPort: 4180
      readinessProbe:                    # Sidecar 可以有自己的 Probe
        httpGet:
          path: /ping
          port: 4180
  containers:
    - name: app
      image: registry.example.com/app:2.0.1
```

> ✅ **原生 Sidecar 解決的問題**：Job 裡的 sidecar 不會讓 Job 卡住；sidecar 會比主容器先就緒；Pod 終止時主容器先停、sidecar 後停，日誌與 Proxy 不會先斷。

#### 3.6.1 容器層級重啟規則（1.35 Beta）

1.35 起可以在**單一容器**上設定 `restartPolicy` 與 `restartPolicyRules`，依結束代碼決定是否原地重啟，不必重建整個 Pod：

```yaml
spec:
  restartPolicy: Never                   # Pod 層級：失敗不重啟
  containers:
    - name: trainer
      image: registry.example.com/ml/trainer:3.1.0
      restartPolicy: Never
      restartPolicyRules:
        - action: Restart                # 只有結束代碼 75（暫時性錯誤）才原地重啟
          exitCodes:
            operator: In
            values: [75]
```

> 📌 1.35 另外新增 `RestartAllContainers` 動作（Alpha，`RestartAllContainersOnContainerExits`），可觸發整個 Pod 原地重啟並重跑 init 容器，主要用於 AI/ML 訓練。正式環境請等 Beta 以後再評估。

---

### 3.7 💡 本章實務建議

1. **每個工作負載都要選對控制器**：無狀態用 Deployment，有狀態優先用 Operator，批次用 Job + `podFailurePolicy`。
2. **企業 Deployment 範本**至少包含：建議標籤、三種 Probe、資源設定、`securityContext`、拓撲分散、`preStop`、`progressDeadlineSeconds`，用 Helm／Kustomize 共用。
3. **Sidecar 一律改用原生 Sidecar**（1.33 GA），尤其是 Job 與 Service Mesh 情境。
4. **批次作業要冪等並設定 TTL**，避免已完成的 Job 與 Pod 堆積在 etcd。
5. **CronJob 明確設定 `timeZone` 與 `concurrencyPolicy`**，重要排程要有漏跑告警。

---

## 4. 服務網路與流量入口

### 4.1 Kubernetes 網路模型

Kubernetes 網路有三條基本規則，由 CNI 負責實現：

1. 每個 Pod 都有自己的 IP，Pod 之間**不經 NAT** 就能互通（跨 Node 也一樣）。
2. Node 上的代理程式（kubelet 等）可以和該 Node 上的所有 Pod 通訊。
3. Pod 看到的自己 IP，就是別人看到的 IP。

```mermaid
flowchart LR
    C["外部用戶端"] --> GW["Gateway / Ingress / LoadBalancer"]
    GW --> SVC["Service（虛擬 IP）"]
    SVC --> ES["EndpointSlice<br/>（Ready 的 Pod IP 清單）"]
    ES --> P1["Pod 10.244.1.12"]
    ES --> P2["Pod 10.244.2.7"]
    P1 -. "DNS 查詢" .-> DNS["CoreDNS"]
```

| 層次 | 負責元件 | 本章章節 |
| --- | --- | --- |
| Pod 網路（L3） | CNI（Cilium／Calico） | [2.3.3](#233-cni-選型與安裝) |
| 服務抽象（L4） | Service、EndpointSlice、kube-proxy | 4.2–4.4 |
| 名稱解析 | CoreDNS | 4.5 |
| 南北向 HTTP／gRPC（L7） | Gateway API、Ingress | 4.6–4.8 |
| 東西向安全 | NetworkPolicy、Service Mesh | 4.9 |

---

### 4.2 Service 類型

```mermaid
flowchart TB
    Client["外部用戶端"] --> LB["LoadBalancer<br/>（雲端 LB / MetalLB）"]
    Client --> NP["NodePort<br/>NodeIP:30000-32767"]
    LB --> CIP["ClusterIP<br/>10.96.x.x"]
    NP --> CIP
    CIP --> P1["Pod 1"]
    CIP --> P2["Pod 2"]
    CIP --> P3["Pod 3"]
```

| 類型 | 用途 | 存取方式 | 正式環境建議 |
| --- | --- | --- | --- |
| **ClusterIP**（預設） | 叢集內部通訊 | `svc.ns.svc.cluster.local` | 內部服務的標準做法 |
| **Headless**（`clusterIP: None`） | 直接回傳 Pod IP | 每個 Pod 有 DNS 記錄 | StatefulSet、用戶端自行負載平衡（gRPC） |
| **NodePort** | 在每個 Node 開放埠 | `<NodeIP>:<NodePort>` | 只用於測試或外部 LB 的後端 |
| **LoadBalancer** | 建立外部 L4 負載平衡器 | 雲端 LB IP／DNS | 雲端環境；地端需搭配 MetalLB、Cilium LB IPAM 或 F5 |
| **ExternalName** | DNS CNAME 到外部名稱 | CNAME | 對外部服務提供叢集內別名（不支援埠對應） |

#### 4.2.1 Service YAML 範例

```yaml
# ClusterIP Service
apiVersion: v1
kind: Service
metadata:
  name: order-service
  namespace: order-prod
spec:
  type: ClusterIP
  selector:
    app.kubernetes.io/name: order-service
  ports:
    - name: http                    # 具名埠，Gateway／ServiceMonitor 都會用到
      port: 80
      targetPort: http              # 對應容器的具名埠
      protocol: TCP
      appProtocol: http             # 讓 Gateway／Mesh 正確判斷協定（http、https、kubernetes.io/h2c）
  trafficDistribution: PreferSameZone   # 1.35 GA：優先同可用區，降低跨區流量費用與延遲
---
# LoadBalancer Service（AWS 內部 NLB，需 AWS Load Balancer Controller）
apiVersion: v1
kind: Service
metadata:
  name: api-gateway
  namespace: edge
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "external"
    service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: "ip"
    service.beta.kubernetes.io/aws-load-balancer-scheme: "internal"
spec:
  type: LoadBalancer
  externalTrafficPolicy: Local       # 保留用戶端來源 IP，並避免多一跳
  selector:
    app.kubernetes.io/name: api-gateway
  ports:
    - name: https
      port: 443
      targetPort: 8443
```

> ⚠️ **v2.0 更正**：v1.0 範例註解寫「AWS ALB 範例」，但 `aws-load-balancer-type: nlb` 建立的是 NLB（L4）；ALB 是 L7，要透過 Ingress 或 Gateway API。AWS Load Balancer Controller 建議改用 `external` + `nlb-target-type`。

#### 4.2.2 trafficDistribution 與流量政策

| 設定 | 說明 | 成熟度 |
| --- | --- | --- |
| `trafficDistribution: PreferSameZone` | 優先送往同可用區的 Endpoint | 1.35 GA（原名 `PreferClose`，已棄用） |
| `trafficDistribution: PreferSameNode` | 優先送往同 Node 的 Endpoint（例如 Node 本地快取） | 1.35 GA |
| `externalTrafficPolicy: Local` | 外部流量只送往本 Node 的 Pod，保留來源 IP | GA |
| `internalTrafficPolicy: Local` | 叢集內流量只送往本 Node 的 Pod | GA |
| `sessionAffinity: ClientIP` | 依用戶端 IP 黏著 | GA |

#### 4.2.3 已棄用：Service `externalIPs`

> ⚠️ **1.36 起棄用**：`spec.externalIPs` 長期有中間人攻擊風險（CVE-2020-8554），1.36 起使用時會出現棄用警告，預計 1.43 移除。請改用 LoadBalancer、NodePort 或 Gateway API。若暫時無法移除，至少用 ValidatingAdmissionPolicy 禁止一般使用者設定此欄位（見 [8.5](#85-admission-控制validatingmutatingadmissionpolicy-與政策引擎)）。

---

### 4.3 EndpointSlice

EndpointSlice（`discovery.k8s.io/v1`，1.21 GA）是 Service 後端清單的正式 API，每個 slice 預設最多 100 個 Endpoint，支援雙堆疊、拓撲提示與 `serving`／`terminating` 狀態。

```bash
# 查看 Service 對應的 EndpointSlice
kubectl get endpointslices -n order-prod -l kubernetes.io/service-name=order-service
kubectl describe endpointslice -n order-prod <slice-name>
```

> ⚠️ **v2.0 更正**：v1.0 用 `kind: Endpoints` 指向外部 IP。**`v1` Endpoints API 自 1.33 起正式棄用**，存取時會出現 `Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice`。手動指向外部 IP 的寫法改為 EndpointSlice，範例見 [13.1](#131-外部資料庫與既有系統)。

---

### 4.4 kube-proxy 模式

| 模式 | 狀態（1.37） | 說明 | 建議 |
| --- | --- | --- | --- |
| `iptables` | GA，Linux 未設定時的預設值 | 規則數隨 Service 線性成長，大叢集更新慢 | 既有叢集可繼續使用 |
| `nftables` | **1.33 GA** | 效能與可擴展性優於 iptables；1.37 進一步優化 | **新叢集建議**（核心 5.13+） |
| `ipvs` | **1.35 起棄用** | 實際上仍依賴 iptables；預計 1.40 預設停用、1.43 移除 | 規劃遷移到 nftables |
| `kernelspace` | Windows | — | — |
| 無 kube-proxy | — | Cilium kube-proxy replacement（eBPF） | 使用 Cilium 時可評估 |

```bash
# 確認目前 kube-proxy 模式（kubeadm 叢集）
kubectl -n kube-system get configmap kube-proxy -o jsonpath='{.data.config\.conf}' | grep 'mode:'
```

> 📌 **1.34 差異**：1.34 的 `ipvs` 尚未棄用，但遷移方向相同；從 iptables／ipvs 切換到 nftables 時，請在維護窗口逐 Node 進行，並清除舊規則（kube-proxy 啟動時會自動清理其他模式留下的規則）。

---

### 4.5 CoreDNS 與服務探索

| 記錄 | 格式 | 範例 |
| --- | --- | --- |
| Service A/AAAA | `<svc>.<ns>.svc.<zone>` | `order-service.order-prod.svc.cluster.local` |
| Headless Pod | `<pod>.<svc>.<ns>.svc.<zone>` | `postgres-0.postgres-headless.data-prod.svc.cluster.local` |
| SRV | `_<port>._<proto>.<svc>.<ns>.svc.<zone>` | `_http._tcp.order-service.order-prod.svc.cluster.local` |

**常見調校**：

- **`ndots:5` 問題**：Pod 預設 `ndots:5`，查詢外部網域（例如 `api.partner.com`）會先嘗試多個叢集內後綴，造成 DNS 查詢量放大。對大量呼叫外部 API 的 Pod，可以設定 `dnsConfig.options: [{name: ndots, value: "2"}]`，或在程式中使用 FQDN（結尾加 `.`）。
- **NodeLocal DNSCache**：在每個 Node 上快取 DNS，降低 CoreDNS 負載與 conntrack 競爭，大型叢集建議啟用（已移到獨立 repo `kubernetes-sigs/node-local-dns`）。
- **CoreDNS 副本**：依 Node 數量水平擴展（可用 cluster-proportional-autoscaler），並設定 PDB 與反親和性。

> ⚠️ **1.37 起 kube-dns 棄用**：預計 1.40 之後不再發布新套件；仍在使用 kube-dns 的叢集請遷移到 CoreDNS。

---

### 4.6 Ingress 與 Ingress Controller

Ingress（`networking.k8s.io/v1`）仍是 **GA 且持續支援**的 API，但功能已凍結，新功能只會加在 Gateway API。

#### 4.6.1 Ingress 架構

```mermaid
flowchart LR
    Internet["Internet"] --> LB["L4 LoadBalancer"]
    LB --> IC["Ingress Controller<br/>（F5 NGINX / Traefik / HAProxy / Kong…）"]
    IC -. "讀取" .-> ING["Ingress 規則"]
    IC --> S1["Service A"]
    IC --> S2["Service B"]
    S1 --> P1["Pod A"]
    S2 --> P2["Pod B"]
```

#### 4.6.2 Ingress NGINX 退役說明（重要）

> ⚠️ **v2.0 更正**：v1.0 推薦的社群版 **Ingress NGINX（`kubernetes/ingress-nginx`）已於 2026-03-24 退役**，GitHub repo 已封存。退役後**不再發布任何版本、bug 修正或安全更新**；既有部署仍能執行，Helm chart 和映像也仍可下載，但持續使用會累積未修補的漏洞風險（例如 2025 年的 CVE-2025-1974「IngressNightmare」）。

| 名稱容易混淆 | 維護者 | 狀態 | annotation 前綴 |
| --- | --- | --- | --- |
| **Ingress NGINX**（`kubernetes/ingress-nginx`） | Kubernetes 社群 | **已退役（2026-03-24）** | `nginx.ingress.kubernetes.io/*` |
| **F5 NGINX Ingress Controller**（`nginx/kubernetes-ingress`） | F5／NGINX | 持續維護（v5.6.3） | `nginx.org/*`、`nginx.com/*` |

官方建議的方向：**優先遷移到 Gateway API**；如果短期內必須繼續使用 Ingress，改用仍在維護的 Ingress Controller。遷移步驟見 [4.8](#48-從-ingress-nginx-遷移到-gateway-api)。

#### 4.6.3 仍在維護的 Ingress Controller 比較（2026-09）

| Controller | 版本 | 特色 | 也支援 Gateway API | 建議場景 |
| --- | --- | --- | --- | --- |
| **F5 NGINX Ingress Controller** | v5.6.3 | 和 NGINX 相容度最高；VirtualServer CRD；NGINX Plus 商業版 | 另有 NGINX Gateway Fabric | 原 NGINX 使用者、需要商業支援 |
| **Traefik Proxy** | v3.7.13 | 設定簡單、Middleware CRD、ACME 自動憑證 | ✅（v1.6 conformant） | 中小型、DevOps 團隊 |
| **HAProxy Kubernetes Ingress** | v3.2.15 | 高效能、熟悉 HAProxy 的團隊 | 部分 | 高吞吐 L7 |
| **Kong Ingress Controller** | 3.5 LTS | API Gateway 功能（認證、限流、Plugin） | ✅ | 需要 API 管理 |
| **Cilium Ingress** | Cilium 1.20 | 內建於 Cilium，不需另裝 | ✅ | 已使用 Cilium |
| **雲端 LB Controller** | — | AWS Load Balancer Controller（ALB）、GKE Ingress、AGC（Azure） | ✅ | 公有雲 |

#### 4.6.4 Ingress 設定範例（F5 NGINX Ingress Controller）

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: main-ingress
  namespace: edge
  annotations:
    nginx.org/client-max-body-size: "50m"     # F5 NGINX 的 annotation 前綴是 nginx.org
    nginx.org/proxy-read-timeout: "60s"
    cert-manager.io/cluster-issuer: "corp-ca-issuer"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - api.example.com
      secretName: api-example-com-tls
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /orders
            pathType: Prefix
            backend:
              service:
                name: order-service
                port:
                  name: http
          - path: /users
            pathType: Prefix
            backend:
              service:
                name: user-service
                port:
                  name: http
```

> 📌 **annotation 不可攜**：不同 Controller 的 annotation 完全不同（`nginx.ingress.kubernetes.io/*` 放到 F5 NGINX 或 Traefik 上會被忽略）。換 Controller 時必須逐一對照，這也是 Gateway API 把常用功能標準化的主要原因。

#### 4.6.5 pathType 說明

| pathType | 比對方式 | 範例：規則 `/orders` |
| --- | --- | --- |
| `Exact` | 完全相同（區分大小寫） | 只符合 `/orders` |
| `Prefix` | 以 `/` 分段的前綴 | 符合 `/orders`、`/orders/1`，不符合 `/ordersX` |
| `ImplementationSpecific` | 由 Controller 決定（可能是 regex） | 不可攜，避免使用 |

---

### 4.7 Gateway API（v1.6）

Gateway API（`gateway.networking.k8s.io`）是 Kubernetes 官方的新一代流量管理 API，以 CRD 形式安裝，**不隨 Kubernetes 版本發布**。目前版本 **v1.6.2**（2026-09-03）。

#### 4.7.1 角色導向的資源模型

```mermaid
flowchart TB
    subgraph Infra["基礎架構提供者"]
        GC["GatewayClass<br/>（例如 eg、cilium、nginx）"]
    end
    subgraph Platform["平台團隊（Namespace: edge）"]
        GW["Gateway<br/>listeners：443/HTTPS、9443/TLS…"]
        LS["ListenerSet<br/>（應用團隊自帶 listener，v1.5 Standard）"]
    end
    subgraph App["應用團隊（Namespace: order-prod）"]
        HR["HTTPRoute"]
        GR["GRPCRoute"]
        SVC["Service"]
    end
    GC --> GW
    LS -. "附掛" .-> GW
    HR -- "parentRefs" --> GW
    GR -- "parentRefs" --> GW
    HR --> SVC
    GR --> SVC
```

| 資源 | 負責角色 | 用途 | Channel（v1.6） |
| --- | --- | --- | --- |
| `GatewayClass` | 基礎架構提供者 | 指定由哪個 Controller 實作 | Standard |
| `Gateway` | 平台／維運團隊 | 定義入口 listener（埠、協定、TLS、允許哪些 Namespace 附掛） | Standard |
| `ListenerSet` | 應用團隊 | 不修改 Gateway 就能新增 listener（多租戶） | Standard（v1.5 起） |
| `HTTPRoute` | 應用團隊 | HTTP 路由、標頭比對、重寫、轉址、權重分流、CORS | Standard |
| `GRPCRoute` | 應用團隊 | gRPC 服務／方法路由 | Standard |
| `TLSRoute` | 應用團隊 | 依 SNI 路由（Passthrough／Terminate） | Standard（v1.5 起） |
| `TCPRoute`／`UDPRoute` | 應用團隊 | L4 路由（資料庫、DNS、IoT） | Standard（v1.6 起） |
| `ReferenceGrant` | 被參照方 | 允許跨 Namespace 參照 Service 或 Secret | Standard（v1） |
| `BackendTLSPolicy` | 應用／資安 | Gateway 到後端使用 TLS | Standard（v1） |

> 🆕 **v1.6 重點**：TCPRoute、UDPRoute 進入 Standard（`v1`），`v1alpha2` 已棄用。之後新的實驗性資源改放在 `gateway.networking.x-k8s.io` 群組，並以 `X` 開頭命名（例如 `XBackend`、`XMesh`），Standard 和 Experimental 的界線更清楚。

#### 4.7.2 安裝 Gateway API CRD 與實作（以 Envoy Gateway 為例）

```bash
# 1. 安裝 Standard channel CRD（正式環境不要裝 experimental）
kubectl apply --server-side -f \
  https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.6.2/standard-install.yaml

# 2. 安裝實作：Envoy Gateway v1.9.2
helm install eg oci://docker.io/envoyproxy/gateway-helm --version v1.9.2 \
  -n envoy-gateway-system --create-namespace

# 3. 確認
kubectl get crd | grep gateway.networking.k8s.io
kubectl get gatewayclass
```

> 📌 許多實作（Cilium、Istio、Envoy Gateway）的 Helm chart 會自帶 CRD。**同一叢集只能有一份 Gateway API CRD**，請由平台團隊統一管理版本，避免不同實作互相覆蓋。

#### 4.7.3 Gateway 與 HTTPRoute 範例

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: eg
spec:
  controllerName: gateway.envoyproxy.io/gatewayclass-controller
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: public-gw
  namespace: edge
spec:
  gatewayClassName: eg
  listeners:
    - name: https
      protocol: HTTPS
      port: 443
      hostname: "*.example.com"
      tls:
        mode: Terminate
        certificateRefs:
          - name: wildcard-example-com-tls
      allowedRoutes:
        namespaces:
          from: Selector
          selector:
            matchLabels:
              gateway-access/public: "true"   # 只有被授權的 Namespace 可以附掛
    - name: http
      protocol: HTTP
      port: 80
      hostname: "*.example.com"
      allowedRoutes:
        namespaces:
          from: Same
---
# HTTP → HTTPS 轉址（放在 edge namespace，附掛到 http listener）
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: https-redirect
  namespace: edge
spec:
  parentRefs:
    - name: public-gw
      sectionName: http
  rules:
    - filters:
        - type: RequestRedirect
          requestRedirect:
            scheme: https
            statusCode: 301
---
# 應用團隊的路由
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: order-api
  namespace: order-prod
spec:
  parentRefs:
    - name: public-gw
      namespace: edge
      sectionName: https
  hostnames:
    - api.example.com
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /orders
      filters:
        - type: CORS
          cors:
            allowOrigins:
              - https://shop.example.com
            allowMethods: ["GET", "POST"]
      timeouts:
        request: 30s
      backendRefs:
        - name: order-service
          port: 80
    - matches:
        - path:
            type: PathPrefix
            value: /v2/orders
      filters:
        - type: URLRewrite
          urlRewrite:
            path:
              type: ReplacePrefixMatch
              replacePrefixMatch: /orders
      backendRefs:
        - name: order-service-v2
          port: 80
```

#### 4.7.4 金絲雀發布（權重分流）與標頭路由

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: order-canary
  namespace: order-prod
spec:
  parentRefs:
    - name: public-gw
      namespace: edge
      sectionName: https
  hostnames:
    - api.example.com
  rules:
    # 內部測試人員帶標頭 X-Canary: true 時一律走新版
    - matches:
        - headers:
            - name: X-Canary
              value: "true"
      backendRefs:
        - name: order-service-v2
          port: 80
    # 其他流量：90% 舊版、10% 新版
    - backendRefs:
        - name: order-service
          port: 80
          weight: 90
        - name: order-service-v2
          port: 80
          weight: 10
```

#### 4.7.5 GRPCRoute、TLSRoute 與 TCPRoute

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: payment-grpc
  namespace: payment-prod
spec:
  parentRefs:
    - name: public-gw
      namespace: edge
      sectionName: https
  hostnames:
    - grpc.example.com
  rules:
    - matches:
        - method:
            service: payment.v1.PaymentService
      backendRefs:
        - name: payment-grpc
          port: 9090
---
# TCPRoute（v1.6 Standard）：Gateway 需有 protocol: TCP 的 listener
apiVersion: gateway.networking.k8s.io/v1
kind: TCPRoute
metadata:
  name: legacy-mq
  namespace: mq-prod
spec:
  parentRefs:
    - name: internal-gw
      namespace: edge
      sectionName: mq-tcp
  rules:
    - backendRefs:
        - name: legacy-mq
          port: 1414
```

#### 4.7.6 跨 Namespace 參照：ReferenceGrant

```yaml
# 允許 edge namespace 的 Gateway 使用 security namespace 中的 TLS Secret
apiVersion: gateway.networking.k8s.io/v1
kind: ReferenceGrant
metadata:
  name: allow-edge-gateway-certs
  namespace: security            # 放在「被參照」的一方
spec:
  from:
    - group: gateway.networking.k8s.io
      kind: Gateway
      namespace: edge
  to:
    - group: ""
      kind: Secret
```

#### 4.7.7 Gateway API 實作選型

| 實作 | 版本（2026-09） | 資料平面 | 備註 |
| --- | --- | --- | --- |
| **Envoy Gateway** | v1.9.2 | Envoy | CNCF Envoy 官方子專案，擴充 Policy（SecurityPolicy、BackendTrafficPolicy） |
| **NGINX Gateway Fabric** | v2.7.2 | NGINX | F5 維護，v1.6 conformant |
| **Cilium** | 1.20.2 | eBPF + Envoy | 已使用 Cilium 時不必另裝 |
| **Istio** | — | Envoy | 同時作為 Mesh 的 Gateway |
| **kgateway** | — | Envoy | CNCF 專案（原 Gloo），v1.6 conformant |
| **Traefik Proxy** | v3.7.13 | Traefik | v1.6 conformant |
| **Kong** | — | Kong（NGINX/OpenResty） | 需要 API 管理功能時 |
| **雲端** | — | GKE Gateway、AWS Gateway API Controller、Azure AGC | 和雲端 LB 整合 |

> 📌 **選型重點**：查看官方 [Implementations](https://gateway-api.sigs.k8s.io/implementations/) 頁面的 conformance 報告，確認實作支援你需要的功能（Extended features，例如 CORS、URLRewrite、BackendTLSPolicy）。

#### 4.7.8 Ingress 與 Gateway API 比較

| 面向 | Ingress | Gateway API |
| --- | --- | --- |
| API 狀態 | GA，功能凍結 | GA（v1），持續演進 |
| 角色分工 | 單一資源，平台與應用混在一起 | GatewayClass／Gateway／Route 分離 |
| 協定 | HTTP(S) | HTTP、gRPC、TLS、TCP、UDP |
| 進階功能 | 靠 annotation（不可攜） | 標準欄位：標頭比對、權重分流、重寫、轉址、CORS、逾時、鏡像 |
| 跨 Namespace | 不支援 | 支援，並以 ReferenceGrant 控管 |
| 多租戶 | 弱 | `allowedRoutes`、ListenerSet |
| 建議 | 既有系統、短期維持 | **新系統首選** |

---

### 4.8 從 Ingress NGINX 遷移到 Gateway API

#### 4.8.1 遷移流程

```mermaid
flowchart TD
    A["盤點<br/>kubectl get ingress -A<br/>列出所有 annotation"] --> B["選定 Gateway API 實作<br/>確認 conformance 與 Extended 功能"]
    B --> C["安裝 CRD 與實作<br/>與 Ingress NGINX 並行"]
    C --> D["ingress2gateway 轉換<br/>人工審查輸出"]
    D --> E["測試環境驗證<br/>以 Host 標頭或測試 DNS"]
    E --> F["正式環境並行<br/>新 LB IP，DNS 權重切換"]
    F --> G["觀察指標與錯誤率"]
    G --> H["移除 Ingress 與舊 Controller"]
```

#### 4.8.2 使用 ingress2gateway

`ingress2gateway`（kubernetes-sigs，v1.0 於 2026-03 發布，最新 v1.2.0）是**遷移助手**：會轉換可支援的設定、標出不支援的 annotation 並提出替代方案，但不是一鍵替換。

```bash
# 安裝
go install github.com/kubernetes-sigs/ingress2gateway@v1.2.0

# 從檔案轉換
ingress2gateway print --providers=ingress-nginx \
  --input-file ingress-prod.yaml > gwapi.yaml

# 從叢集中的某個 namespace 轉換
ingress2gateway print --providers=ingress-nginx -n order-prod > gwapi-order.yaml

# 從整個叢集轉換；--emitter 可輸出特定實作的擴充資源（預設 standard）
ingress2gateway print --providers=ingress-nginx -A --emitter=standard > gwapi-all.yaml
```

> 📌 支援的 provider 包含 `ingress-nginx`、`nginx`（F5）、`kong`、`traefik`、`istio`、`cilium`、`apisix`、`gce`、`openapi3`。輸出結果**一定要人工審查**，尤其是 regex 路徑、snippet 與認證相關設定。

#### 4.8.3 常見 annotation 對照表

| Ingress NGINX annotation | Gateway API 對應做法 |
| --- | --- |
| `ssl-redirect` ／ `force-ssl-redirect` | HTTP listener 上的 HTTPRoute `RequestRedirect`（scheme: https） |
| `rewrite-target` | `URLRewrite` filter（`ReplacePrefixMatch`／`ReplaceFullPath`） |
| `use-regex` + regex 路徑 | `PathPrefix`／`Exact` 重新設計；`RegularExpression` 是 Implementation-specific |
| `canary`、`canary-weight`、`canary-by-header` | `backendRefs[].weight`、`matches.headers` |
| `enable-cors`、`cors-allow-origin` | `CORS` filter（v1.5 起 Standard） |
| `proxy-read-timeout`、`proxy-send-timeout` | `rules[].timeouts.request`／`backendRequest` |
| `proxy-body-size` | 實作專屬 Policy（例如 Envoy Gateway `ClientTrafficPolicy`） |
| `auth-url`、`auth-signin`（外部認證） | 實作專屬 Policy（例如 Envoy Gateway `SecurityPolicy`）或 Service Mesh |
| `limit-rps`、`limit-connections` | 實作專屬 Policy（例如 `BackendTrafficPolicy`） |
| `backend-protocol: HTTPS/GRPC` | `BackendTLSPolicy`、GRPCRoute、Service `appProtocol` |
| `configuration-snippet`、`server-snippet` | **沒有對應**：重新設計；snippet 本身也是重大安全風險 |
| `whitelist-source-range` | 實作專屬 Policy 或 NetworkPolicy／雲端 LB 安全群組 |

> ⚠️ **注意：Ingress NGINX 的五個隱性行為**（官方部落格〈Before You Migrate〉整理），轉換後務必逐一測試：
>
> 1. regex 比對是**前綴比對且不分大小寫**；Envoy 系實作（Istio、Envoy Gateway、kgateway）是完整且區分大小寫的比對。
> 2. 只要同一個 host 有任一 Ingress 設定 `use-regex: "true"`，該 host 在**所有** Ingress 上的路徑都會被當成 regex。
> 3. 設定 `rewrite-target` 會隱含啟用 regex。
> 4. 缺少尾端斜線的請求會被轉址到加上斜線的路徑。
> 5. Ingress NGINX 會正規化 URL（例如合併重複斜線）。

---

### 4.9 NetworkPolicy 基礎

NetworkPolicy 是 Namespace 範圍的 L3/L4 防火牆規則，**需要 CNI 支援**（Cilium、Calico 支援；Flannel 不支援）。

**核心規則**：

- Pod 沒有被任何 NetworkPolicy 選中時，**允許所有流量**。
- 一旦被選中，就只允許 policy 明確列出的流量（白名單）；多個 policy 是聯集。
- `Ingress` 與 `Egress` 分開計算；限制 Egress 時記得放行 DNS。

```yaml
# 1. Namespace 預設全部拒絕（進出都擋）
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: order-prod
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
---
# 2. 放行所有 Pod 到 CoreDNS
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns-egress
  namespace: order-prod
spec:
  podSelector: {}
  policyTypes: ["Egress"]
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: kube-system
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
---
# 3. 只允許 Gateway 所在的 namespace 存取 order-service
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-gateway
  namespace: order-prod
spec:
  podSelector:
    matchLabels:
      app.kubernetes.io/name: order-service
  policyTypes: ["Ingress"]
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: edge
      ports:
        - protocol: TCP
          port: 8080
```

> 📌 `kubernetes.io/metadata.name` 是每個 Namespace 都有的自動標籤（1.22 GA），選擇 Namespace 時建議用它。進階需求（FQDN 白名單、L7、叢集層級政策）可使用 Cilium／Calico 的擴充 CRD，或 SIG Network 的 network-policy-api 專案（v0.2.0 已把 AdminNetworkPolicy／BaselineAdminNetworkPolicy 合併為 `ClusterNetworkPolicy`，仍是 v1alpha2，正式環境請先評估實作支援度）。

---

### 4.10 💡 本章實務建議

1. **新系統一律採用 Gateway API**，Ingress 只用於既有系統；**Ingress NGINX 必須排入遷移計畫**，並列入資安風險清單。
2. **Gateway API CRD 由平台團隊統一管理版本**，只安裝 Standard channel。
3. **Gateway 歸平台團隊、Route 歸應用團隊**：用 `allowedRoutes` + Namespace 標籤控管誰能附掛。
4. **新叢集使用 nftables 或 eBPF**，既有 `ipvs` 叢集在 1.40 前完成遷移。
5. **移除 `externalIPs` 與 Endpoints 的使用**，改用 LoadBalancer／Gateway 與 EndpointSlice。
6. **每個 Namespace 都要有 default-deny NetworkPolicy**，再逐一放行。

---

## 5. 設定與儲存管理

### 5.1 ConfigMap

ConfigMap 存放**非機密**設定（每個物件上限 1 MiB）。設定和映像分離後，同一個映像可以部署到不同環境。

#### 5.1.1 ConfigMap 定義與四種使用方式

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: order-service-config
  namespace: order-prod
data:
  LOG_LEVEL: "INFO"
  MAX_CONNECTIONS: "100"
  application.yaml: |
    server:
      port: 8080
      shutdown: graceful
    spring:
      datasource:
        url: jdbc:postgresql://postgres-headless.data-prod:5432/orders
---
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
  namespace: order-prod
spec:
  containers:
    - name: app
      image: registry.example.com/ecommerce/order-service:1.4.2
      env:
        # 方式一：單一環境變數
        - name: LOG_LEVEL
          valueFrom:
            configMapKeyRef:
              name: order-service-config
              key: LOG_LEVEL
      # 方式二：所有 key 作為環境變數
      envFrom:
        - configMapRef:
            name: order-service-config
          prefix: CFG_
      # 方式三：掛載為檔案（更新後約 1 分鐘內同步到容器內）
      volumeMounts:
        - name: config-volume
          mountPath: /app/config
          readOnly: true
  volumes:
    - name: config-volume
      configMap:
        name: order-service-config
        items:
          - key: application.yaml
            path: application.yaml
```

| 使用方式 | 更新後是否自動生效 | 說明 |
| --- | --- | --- |
| 環境變數（`env`／`envFrom`） | ❌ 需要重啟 Pod | 最常見，但修改後要 `kubectl rollout restart` |
| Volume 掛載 | ✅ kubelet 定期同步（約 1 分鐘內） | 應用需自行重新讀取；**使用 `subPath` 掛載時不會更新** |
| 指令參數 | ❌ | 透過 `$(VAR)` 引用環境變數 |
| 程式透過 API 讀取 | ✅ | 需要 RBAC 權限，耦合 Kubernetes API |

> 📌 **建議做法**：設定變更走 GitOps，並讓 Pod template 帶上設定內容的雜湊值（Helm 的 `checksum/config` 註解、Kustomize 的 `configMapGenerator` 自動加後綴），設定一改就觸發滾動更新，行為可預期、可回滾。

#### 5.1.2 Immutable ConfigMap／Secret

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: order-service-config-v7     # 以版本命名，變更時建立新物件
immutable: true                     # 1.21 GA：不可修改，kubelet 也不再 watch
data:
  LOG_LEVEL: "INFO"
```

大型叢集中大量 ConfigMap／Secret 被 watch 會對 API Server 造成負擔，設定為 `immutable` 可以降低負載，也能避免誤改正式設定。

#### 5.1.3 從檔案載入環境變數（1.35 Beta）

1.34 新增、1.35 進入 Beta 的 `EnvFiles` 功能，可以讓 init 容器產生 `.env` 檔，再由主容器透過 `fileKeyRef` 讀成環境變數（主容器不需要掛載該 Volume）：

```yaml
spec:
  initContainers:
    - name: render-env
      image: registry.example.com/tools/config-renderer:1.2.0
      volumeMounts:
        - name: envdir
          mountPath: /data
  containers:
    - name: app
      image: registry.example.com/app:2.0.1
      env:
        - name: DB_ADDRESS
          valueFrom:
            fileKeyRef:
              volumeName: envdir
              path: config.env
              key: DB_ADDRESS
              optional: false
  volumes:
    - name: envdir
      emptyDir: {}
```

> ⚠️ `emptyDir` 沒有 Secret 的保護機制（加密、RBAC），**不要用這個功能傳遞機密**。

---

### 5.2 Secret

#### 5.2.1 Secret 類型與定義

| 類型 | 用途 |
| --- | --- |
| `Opaque` | 一般機密（預設） |
| `kubernetes.io/tls` | TLS 憑證（`tls.crt`、`tls.key`） |
| `kubernetes.io/dockerconfigjson` | 私有 Registry 認證（`imagePullSecrets`） |
| `kubernetes.io/basic-auth`、`kubernetes.io/ssh-auth` | 帳密、SSH 金鑰 |
| `kubernetes.io/service-account-token` | 舊式長效 SA Token（**不建議**，見 8.3） |

```yaml
# data 欄位需要 Base64；Base64 是「編碼」不是「加密」
apiVersion: v1
kind: Secret
metadata:
  name: order-db-credentials
  namespace: order-prod
type: Opaque
data:
  username: b3JkZXJfYXBw            # echo -n 'order_app' | base64
---
# stringData 可以直接寫明文，API Server 會自動編碼（僅用於本機測試，不可提交到 Git）
apiVersion: v1
kind: Secret
metadata:
  name: order-db-credentials-dev
  namespace: order-dev
type: Opaque
stringData:
  username: order_app
  password: change-me
```

```bash
# 建立 TLS Secret 與 Registry Secret
kubectl create secret tls api-example-com-tls -n edge --cert=tls.crt --key=tls.key
kubectl create secret docker-registry regcred -n order-prod \
  --docker-server=registry.example.com --docker-username=robot\$ci --docker-password='***'
```

#### 5.2.2 Secret 安全建議

> ⚠️ **v2.0 更正**：v1.0 寫「預設 Secret 在 etcd 中未加密」，這句話仍然正確，但只說了一半。本版補充完整的防護層次：

| 層次 | 措施 | 章節 |
| --- | --- | --- |
| 靜態加密 | API Server `EncryptionConfiguration` + **KMS v2**（1.29 GA）串接 HSM／雲端 KMS | [8.6](#86-secret-靜態加密kms-v2) |
| 存取控制 | RBAC 最小權限；`get`／`list`／`watch` Secret 等同讀取明文 | [8.2](#82-rbac-權限控管) |
| 不放進 Git | External Secrets Operator（推薦）、Sealed Secrets、SOPS | [13.3](#133-external-secrets-operator-與-vault) |
| 減少暴露 | 以 Volume 掛載取代環境變數（環境變數容易出現在日誌或 crash dump） | — |
| 稽核 | Audit Policy 記錄 Secret 存取（只記 Metadata，不要記錄內容） | [8.9](#89-audit-log稽核日誌) |
| 映像拉取 | 1.35 起 kubelet 會驗證快取映像的拉取憑證（`KubeletEnsureSecretPulledImages` Beta），避免其他 Pod 借用已拉下的私有映像 | [8.10](#810-供應鏈安全) |

---

### 5.3 Volume 類型總覽

| 類型 | 生命週期 | 典型用途 |
| --- | --- | --- |
| `emptyDir` | 與 Pod 相同 | 暫存、容器間共享；可設 `medium: Memory` 與 `sizeLimit` |
| `configMap`／`secret`／`downwardAPI` | 與 Pod 相同 | 設定與中繼資料注入 |
| `projected` | 與 Pod 相同 | 把多個來源（含 SA Token、ClusterTrustBundle、Pod 憑證）合併到同一目錄 |
| `persistentVolumeClaim` | 獨立於 Pod | 永久資料 |
| `ephemeral`（Generic Ephemeral Volume） | 與 Pod 相同，但由 CSI 動態佈建 | 需要大容量暫存空間 |
| `image`（1.36 GA） | 與 Pod 相同 | 把 OCI 映像／Artifact 唯讀掛載（模型、資料集、靜態檔） |
| `hostPath` | 與 Node 相同 | 系統 Agent 專用，**一般應用禁止使用** |

> ⚠️ **1.36 起移除 `gitRepo` Volume**：`gitRepo` 自 1.11 棄用，1.36 永久停用（有以 root 身分在 Node 上執行程式碼的風險）。請改用 init 容器或 `git-sync` sidecar。

#### 5.3.1 Image Volume（1.36 GA）

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: inference
spec:
  containers:
    - name: server
      image: registry.example.com/ml/inference-server:4.2.0
      volumeMounts:
        - name: model
          mountPath: /models/fraud-detect
          readOnly: true
  volumes:
    - name: model
      image:
        reference: registry.example.com/ml/models/fraud-detect:2026.09   # 模型以 OCI artifact 發佈
        pullPolicy: IfNotPresent
```

> 📌 需要 Container Runtime 支援（containerd 2.1 以上、或對應版本的 CRI-O）。模型或資料和應用映像分開版本管理，可以分別更新、分別掃描。

---

### 5.4 PersistentVolume、PVC 與 StorageClass

#### 5.4.1 動態佈建架構

```mermaid
flowchart LR
    Dev["應用團隊"] -- "建立" --> PVC["PersistentVolumeClaim<br/>100Gi, RWO, fast-ssd"]
    PVC -- "引用" --> SC["StorageClass fast-ssd<br/>provisioner: ebs.csi.aws.com"]
    SC -- "CSI Controller 建立磁碟" --> PV["PersistentVolume"]
    PV -- "綁定" --> PVC
    Pod["Pod"] -- "掛載" --> PVC
    PV -- "CSI Node 掛載到 Node" --> Node["Worker Node"]
```

#### 5.4.2 StorageClass 與 PVC 範例

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
provisioner: ebs.csi.aws.com            # 地端常見：Ceph RBD（rook）、vSphere CSI、NetApp Trident、Portworx
parameters:
  type: gp3
  encrypted: "true"
reclaimPolicy: Retain                   # 正式資料建議 Retain，避免刪除 PVC 時資料一起消失
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer # 等 Pod 排程後才在同一可用區建立磁碟
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: report-data
  namespace: batch-prod
spec:
  accessModes: ["ReadWriteOncePod"]     # 1.29 GA：整個叢集只能有一個 Pod 掛載
  storageClassName: fast-ssd
  resources:
    requests:
      storage: 200Gi
```

#### 5.4.3 存取模式與回收策略

| 存取模式 | 縮寫 | 說明 |
| --- | --- | --- |
| `ReadWriteOnce` | RWO | 單一 **Node** 可讀寫（同 Node 的多個 Pod 可共用） |
| `ReadWriteOncePod` | RWOP | 單一 **Pod** 可讀寫（1.29 GA，資料庫建議） |
| `ReadOnlyMany` | ROX | 多 Node 唯讀 |
| `ReadWriteMany` | RWX | 多 Node 讀寫（NFS、CephFS、EFS、Azure Files） |

| reclaimPolicy | 刪除 PVC 後 | 建議 |
| --- | --- | --- |
| `Delete` | PV 與實體磁碟一起刪除 | 開發／暫存環境 |
| `Retain` | PV 變成 `Released`，資料保留，需人工處理 | 正式環境 |

#### 5.4.4 線上擴容與失敗復原

```bash
# 修改 PVC 容量即可（StorageClass 需 allowVolumeExpansion: true）
kubectl patch pvc report-data -n batch-prod -p '{"spec":{"resources":{"requests":{"storage":"300Gi"}}}}'
kubectl get pvc report-data -n batch-prod -o jsonpath='{.status.conditions}'
```

- **1.34 GA**：擴容失敗（例如超過配額）時，可以把容量改回較小但仍大於原始容量的值重試，不必再找管理員手動處理。
- 容量**只能增加不能縮小**。

#### 5.4.5 VolumeAttributesClass（1.34 GA）

不必重建 PVC，就能修改磁碟的 IOPS、吞吐量等屬性（需 CSI 驅動支援 `ModifyVolume`）：

```yaml
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: gold
driverName: ebs.csi.aws.com
parameters:
  iops: "8000"
  throughput: "500"
---
# 在 PVC 指定（或之後修改）volumeAttributesClassName
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-data
spec:
  accessModes: ["ReadWriteOncePod"]
  storageClassName: fast-ssd
  volumeAttributesClassName: gold
  resources:
    requests:
      storage: 500Gi
```

#### 5.4.6 找出閒置的 PVC（1.37 Beta）

1.37 起 PVC 會有 `Unused` condition（`PersistentVolumeClaimUnusedSinceTime`，Beta 預設開啟），可以依 `lastTransitionTime` 找出長期沒有 Pod 使用的 PVC，作為成本清理依據：

```bash
kubectl get pvc -A -o json | jq -r '.items[]
  | select(.status.conditions[]? | select(.type=="Unused" and .status=="True"))
  | "\(.metadata.namespace)/\(.metadata.name)"'
```

---

### 5.5 VolumeSnapshot 與 VolumeGroupSnapshot

快照 API 由 CSI **external-snapshotter**（v8.6.0）提供 CRD 與控制器，**需要另外安裝**，CSI 驅動也必須支援。

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: ebs-snapclass
driver: ebs.csi.aws.com
deletionPolicy: Retain
---
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: db-data-20261001
  namespace: data-prod
spec:
  volumeSnapshotClassName: ebs-snapclass
  source:
    persistentVolumeClaimName: db-data
---
# 從快照還原成新的 PVC
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-data-restore
  namespace: data-prod
spec:
  accessModes: ["ReadWriteOncePod"]
  storageClassName: fast-ssd
  dataSource:
    apiGroup: snapshot.storage.k8s.io
    kind: VolumeSnapshot
    name: db-data-20261001
  resources:
    requests:
      storage: 500Gi
```

**VolumeGroupSnapshot（1.36 GA，`groupsnapshot.storage.k8s.io/v1`）**：對多個 PVC 同時建立「當機一致性」快照，適合資料與 WAL 分開存放的資料庫：

```yaml
apiVersion: groupsnapshot.storage.k8s.io/v1
kind: VolumeGroupSnapshot
metadata:
  name: pg-group-20261001
  namespace: data-prod
spec:
  volumeGroupSnapshotClassName: csi-group-snapclass
  source:
    selector:
      matchLabels:
        app.kubernetes.io/name: postgres   # 選取同一組 PVC
```

> ⚠️ **快照不等於備份**：快照通常和原始磁碟在同一個儲存系統或區域。正式環境需要搭配 Velero 等工具，把資料複製到異地或物件儲存（見 [10.5](#105-災難復原與-velero)）。

---

### 5.6 💡 本章實務建議

1. **設定變更走 GitOps + 雜湊觸發滾動更新**，不要依賴 Volume 自動更新來「熱更新」正式環境。
2. **Secret 不進 Git**：統一採用 External Secrets Operator 串接 Vault／雲端 Secret Manager，並啟用 KMS v2。
3. **正式資料使用 `Retain` + `WaitForFirstConsumer`**，資料庫使用 `ReadWriteOncePod`。
4. **儲存效能需求用 VolumeAttributesClass 分級**（銀、金、白金），取代為每種效能建立一個 StorageClass。
5. **定期清理 `Unused` PVC 與 `Released` PV**，納入每月成本檢視。
6. **快照 + 異地備份 + 還原演練**三者缺一不可。

---

## 6. 資源管理、排程與自動擴縮

### 6.1 Resource Request / Limit 與 QoS

#### 6.1.1 Request 與 Limit 的意義

| 設定 | 誰會用到 | 效果 |
| --- | --- | --- |
| `requests.cpu` | Scheduler、CFS 權重 | 排程依據；CPU 爭用時依比例分配 |
| `requests.memory` | Scheduler、驅逐順序 | 排程依據；Node 記憶體壓力時，超過 request 的 Pod 先被驅逐 |
| `limits.cpu` | CFS quota | 超過即被**節流（throttling）**，不會被殺 |
| `limits.memory` | cgroup | 超過即被 **OOMKilled** |

```yaml
resources:
  requests:
    cpu: "500m"       # 0.5 vCPU
    memory: "1Gi"
  limits:
    memory: "1Gi"     # 記憶體 limit = request，行為可預期
    # cpu limit 視情況設定（見 6.1.3）
```

#### 6.1.2 CPU 與 Memory 單位

| 資源 | 單位 | 說明 |
| --- | --- | --- |
| CPU | `1` = 1 vCPU；`500m` = 0.5 vCPU | 最小 `1m` |
| Memory | `Ki`、`Mi`、`Gi`（二進位）；`K`、`M`、`G`（十進位） | `1Gi` = 1024³ bytes，`1G` = 1000³ bytes；**注意不要寫成 `1m`（千分之一 byte）** |

#### 6.1.3 QoS 等級與 CPU limit 的取捨

| QoS | 條件 | 記憶體壓力時的驅逐順序 |
| --- | --- | --- |
| **Guaranteed** | 每個容器 CPU 與 Memory 的 request = limit | 最後 |
| **Burstable** | 至少有一個 request 或 limit，但不符合 Guaranteed | 中間 |
| **BestEffort** | 完全沒有設定 | 最先 |

**CPU limit 該不該設？**

| 做法 | 優點 | 缺點 | 適用 |
| --- | --- | --- | --- |
| 不設 CPU limit | 閒置 CPU 可被利用，避免 CFS 節流造成延遲尖峰 | 需要靠 request 與 Quota 控管 | 延遲敏感的線上服務（多數 API） |
| CPU limit = request（Guaranteed） | 效能可預測；可搭配 CPU Manager static 綁核 | 資源利用率低 | 低延遲交易、計費核心 |
| CPU limit > request | 允許有限度突發 | 仍可能節流 | 多租戶、需要限制「吵鬧鄰居」 |

> ⚠️ **v2.0 更正**：v1.0 建議 Java 應用「Limit 為 Request 的 1.5–2 倍」（包含 Memory）。記憶體 limit 大於 request 時，Node 記憶體不足就會優先驅逐這些 Pod，而且 JVM heap 若依 limit 計算，實際使用可能遠超過 request。本版建議 **Memory limit = request**，並用 `-XX:MaxRAMPercentage` 讓 JVM 依容器限制自動計算 heap。

#### 6.1.4 資源設定建議

```mermaid
flowchart LR
    A["上線前壓測<br/>取得基準值"] --> B["設定 request<br/>≈ P95 使用量"]
    B --> C["Memory limit = request<br/>CPU 依政策"]
    C --> D["VPA 建議模式<br/>持續觀察"]
    D --> E["每季檢討<br/>調整 request"]
    E --> B
```

| 工作負載 | CPU request | Memory | 備註 |
| --- | --- | --- | --- |
| Java（Spring Boot） | 穩態 P95 使用量 | limit = request；`MaxRAMPercentage=75` | 啟動時 CPU 需求高，可搭配 startupProbe 或 in-place resize |
| Node.js／Go | 穩態 P95 使用量 | limit = request | Node.js 注意 `--max-old-space-size` |
| 批次作業 | 依吞吐需求 | limit = request | 可用較低 PriorityClass 吃閒置資源 |

#### 6.1.5 Pod 層級資源（1.34 Beta）

1.34 起可以在 **Pod 層級**設定總資源（`spec.resources`），讓 Pod 內多個容器共享預算，不必逐一切分：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecars
spec:
  resources:                   # Pod 整體預算
    requests:
      cpu: "1"
      memory: 2Gi
    limits:
      memory: 2Gi
  containers:
    - name: app
      image: registry.example.com/app:2.0.1
    - name: helper
      image: registry.example.com/helper:1.1.0
```

> 📌 1.36 起 Pod 層級資源也可以原地調整（Beta）；1.37 起 Pod 層級的資源管理器（CPU／Memory Manager）進入 Beta。目前仍是 Beta，正式環境導入前先在測試環境驗證。

#### 6.1.6 原地調整 Pod 資源（In-place Resize，1.35 GA）

不重建 Pod 就能調整 CPU／Memory，適合 Java 啟動時需要較多 CPU、穩定後降低的情境：

```yaml
containers:
  - name: app
    image: registry.example.com/app:2.0.1
    resizePolicy:
      - resourceName: cpu
        restartPolicy: NotRequired        # CPU 調整不重啟
      - resourceName: memory
        restartPolicy: RestartContainer   # 記憶體調整時重啟容器（JVM heap 需要重新計算）
    resources:
      requests:
        cpu: "2"
        memory: 2Gi
      limits:
        memory: 2Gi
```

```bash
# 透過 resize subresource 調整（kubectl 1.32+）
kubectl patch pod app-7d9f-abcde -n order-prod --subresource resize \
  -p '{"spec":{"containers":[{"name":"app","resources":{"requests":{"cpu":"500m"}}}]}}'

# 查看調整狀態（PodResizePending / PodResizeInProgress condition）
kubectl get pod app-7d9f-abcde -n order-prod -o jsonpath='{.status.conditions}'
```

> 📌 **1.34 差異**：1.34 為 Beta（預設開啟）；1.35 GA 後支援降低記憶體 limit（會檢查目前使用量）。原地調整只改變 Pod，**不會回寫 Deployment**，下次滾動更新會回到 template 的值，因此通常搭配 VPA 使用。

---

### 6.2 Health Check：Liveness／Readiness／Startup Probe

#### 6.2.1 三種 Probe 比較

| Probe | 問的問題 | 失敗後果 | 設計原則 |
| --- | --- | --- | --- |
| **Startup** | 啟動完成了嗎？ | 未成功前不執行其他 Probe；超過門檻則重啟 | 給啟動慢的應用足夠時間 |
| **Liveness** | 程式還活著嗎（是否卡死）？ | 重啟容器 | **只檢查自身**，不要檢查資料庫等外部依賴 |
| **Readiness** | 現在能接流量嗎？ | 從 EndpointSlice 移除（不重啟） | 可以檢查關鍵依賴；暫時過載時回報 not ready |

#### 6.2.2 Probe 方式

```yaml
# HTTP GET（最常見）
livenessProbe:
  httpGet:
    path: /actuator/health/liveness
    port: 8080

# TCP Socket
readinessProbe:
  tcpSocket:
    port: 5432

# Exec（會在容器內 fork 程序，頻繁執行有成本）
livenessProbe:
  exec:
    command: ["pg_isready", "-U", "postgres"]

# gRPC（1.27 GA；應用需實作 gRPC Health Checking Protocol）
livenessProbe:
  grpc:
    port: 9090
    service: liveness        # 選填：對應 health check 的 service 名稱
```

> ⚠️ **v2.0 更正**：v1.0 把 gRPC Probe 標示為「Kubernetes 1.24+」。1.24 是 Beta，**1.27 才 GA**。v1.0 範例在 HTTP 標頭放 `Authorization: Bearer xxx` 也不建議：Probe 端點應免認證，並只在內部埠提供。
>
> 📌 **1.34 Pod Security 變更**：自 1.34 起，Pod 要符合 `restricted` 標準，Probe 與 lifecycle handler **不得設定 `host` 欄位**（避免被用來探測外部主機或 Node 本機，繞過安全控管）。Probe 一律檢查 Pod 本身即可。

#### 6.2.3 常見 Probe 設定錯誤

| 錯誤 | 後果 | 建議 |
| --- | --- | --- |
| 用很長的 `initialDelaySeconds` 等啟動 | 啟動慢時仍被重啟；啟動快時浪費時間 | 改用 startupProbe |
| Liveness 檢查資料庫等外部依賴 | 依賴故障時所有 Pod 被重啟，造成連鎖故障 | Liveness 只檢查自身 |
| 沒有 Readiness | 啟動中或關閉中仍收到流量 | 一定要設定 |
| `timeoutSeconds` 預設 1 秒 | 高負載或 GC 時誤判 | 設為 2–5 秒 |
| Liveness 和 Readiness 用同一個端點、相同門檻 | 流量尖峰時被當成死掉而重啟 | Liveness 門檻應更寬鬆 |

---

### 6.3 排程控制

#### 6.3.1 排程機制總覽

| 機制 | 作用 | 範例 |
| --- | --- | --- |
| `nodeSelector` | 只能排到有特定標籤的 Node | `node.kubernetes.io/instance-type: m7i.2xlarge` |
| Node Affinity | 較彈性的 Node 條件（必須／偏好） | 偏好 SSD Node |
| Pod Affinity／Anti-affinity | 和其他 Pod 放在一起／分開 | 同一服務的副本分散 |
| `topologySpreadConstraints` | 按拓撲網域平均分散 | 跨可用區、跨 Node |
| Taints／Tolerations | Node 排斥 Pod，除非 Pod 容忍 | GPU Node、專屬租戶 Node |
| PriorityClass | 優先順序與搶占 | 關鍵服務優先 |
| Scheduling Gates | 先建立 Pod，條件滿足才排程 | 等配額或外部核准（Kueue） |

#### 6.3.2 Node Affinity 與 Taints

```yaml
# Node：標記為金融核心專用，並加上污點
# kubectl label node worker-31 example.com/pool=core-banking
# kubectl taint node worker-31 example.com/dedicated=core-banking:NoSchedule
spec:
  tolerations:
    - key: example.com/dedicated
      operator: Equal
      value: core-banking
      effect: NoSchedule
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: example.com/pool
                operator: In
                values: ["core-banking"]
```

> 📌 **專屬節點要同時用「污點 + 親和性」**：污點只能擋住別人，親和性才能確保自己一定排過去。

#### 6.3.3 PriorityClass 與搶占

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: business-critical
value: 100000
globalDefault: false
preemptionPolicy: PreemptLowerPriority
description: "核心交易服務，資源不足時可搶占低優先序工作"
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: batch-low
value: 1000
preemptionPolicy: Never          # 不搶占別人，只用閒置資源
description: "批次作業"
```

> ⚠️ 不要隨意使用 `system-cluster-critical`／`system-node-critical`，它們保留給叢集元件。PriorityClass 應搭配 ResourceQuota（`scopeSelector`）限制誰能使用高優先序。

#### 6.3.4 Pod Disruption Budget（PDB）

PDB 限制**自願性中斷**（drain、升級、Cluster Autoscaler 縮減 Node）時同時被驅逐的 Pod 數量：

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: order-service-pdb
  namespace: order-prod
spec:
  maxUnavailable: 1                 # 副本數會變動時，maxUnavailable 比 minAvailable 更不易卡住
  unhealthyPodEvictionPolicy: AlwaysAllow   # 1.31 GA：已經不健康的 Pod 可直接驅逐，避免 drain 卡死
  selector:
    matchLabels:
      app.kubernetes.io/name: order-service
```

> ⚠️ 單副本服務設定 `minAvailable: 1` 會讓 Node 永遠無法 drain，升級時一定會卡住。單副本服務要嘛提高副本數，要嘛接受短暫中斷。

---

### 6.4 自動擴縮

```mermaid
flowchart TB
    M["指標來源<br/>metrics-server / Prometheus Adapter / KEDA"] --> HPA["HPA<br/>水平：增減 Pod 數"]
    M --> VPA["VPA<br/>垂直：調整 request"]
    HPA --> P["Pending Pod"]
    P --> CA["Cluster Autoscaler / Karpenter<br/>增加 Node"]
    CA --> N["新 Node"]
```

| 元件 | 調整對象 | 依據 | 備註 |
| --- | --- | --- | --- |
| **HPA** | Pod 副本數 | CPU、Memory、自訂、外部指標 | 內建（`autoscaling/v2`） |
| **VPA**（1.8.0） | Pod request／limit | 歷史使用量 | 需另外安裝；支援 `InPlaceOrRecreate` |
| **KEDA**（2.21.0） | Pod 副本數（含 0） | 70+ 種事件來源（Kafka lag、佇列長度、Cron） | CNCF 畢業專案 |
| **Cluster Autoscaler** | Node 數 | Pending Pod、低使用率 Node | 依雲端 Node Group |
| **Karpenter**（1.14） | Node 數與規格 | Pending Pod 的需求 | 直接選擇最適合的機型；AWS／Azure |

#### 6.4.1 HPA（autoscaling/v2）

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-service-hpa
  namespace: order-prod
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-service
  minReplicas: 3
  maxReplicas: 30
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70        # 相對於 request 的百分比
    - type: Pods                        # 自訂指標（需要 Prometheus Adapter 等）
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: "200"
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 0
      tolerance: 0.05                   # 1.35 Beta、1.37 GA：可自訂容忍度（預設 10%）
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
        - type: Pods
          value: 4
          periodSeconds: 15
      selectPolicy: Max
    scaleDown:
      stabilizationWindowSeconds: 300   # 縮容冷卻 5 分鐘
      policies:
        - type: Percent
          value: 10
          periodSeconds: 60
```

```bash
kubectl get hpa -n order-prod
kubectl describe hpa order-service-hpa -n order-prod   # 看 Conditions：AbleToScale / ScalingActive / ScalingLimited
```

> ⚠️ **v2.0 更正**：v1.0 範例同時以 Memory 使用率擴展 Java 服務。JVM 很少把記憶體歸還給 OS，記憶體使用率幾乎不會下降，HPA 擴出去後很難縮回。Java 服務建議以 CPU、RPS 或延遲指標擴展。另外要注意：**HPA 和 VPA 不要同時依 CPU／Memory 調整同一個工作負載**。

#### 6.4.2 HPA 縮到 0（1.37 Beta）

1.37 起 `HPAScaleToZero` 預設開啟，`minReplicas: 0` 搭配**至少一個 Object 或 External 指標**（例如佇列長度）即可縮到 0：

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: queue-worker
  namespace: batch-prod
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: queue-worker
  minReplicas: 0
  maxReplicas: 10
  metrics:
    - type: External
      external:
        metric:
          name: queue_consumer_lag
          selector:
            matchLabels:
              queue: settlement-tasks
        target:
          type: Value
          value: "30"
```

> 📌 HPA 透過 `ScaledToZero` condition 記錄「是自己縮到 0 的」，**不會喚醒被人工設為 0 的工作負載**。1.34–1.36 需要縮到 0 時，請使用 KEDA。

#### 6.4.3 KEDA 事件驅動擴展

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: settlement-consumer
  namespace: batch-prod
spec:
  scaleTargetRef:
    name: settlement-consumer
  minReplicaCount: 0
  maxReplicaCount: 20
  cooldownPeriod: 300
  triggers:
    - type: kafka
      metadata:
        bootstrapServers: kafka-bootstrap.kafka:9092
        consumerGroup: settlement
        topic: settlement-events
        lagThreshold: "100"
```

#### 6.4.4 VPA

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: order-service-vpa
  namespace: order-prod
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-service
  updatePolicy:
    updateMode: "Off"              # 先用建議模式；成熟後改 InPlaceOrRecreate
  resourcePolicy:
    containerPolicies:
      - containerName: "*"
        controlledResources: ["cpu", "memory"]
        minAllowed:
          cpu: 100m
          memory: 256Mi
        maxAllowed:
          cpu: "4"
          memory: 8Gi
```

#### 6.4.5 Node 自動擴縮：Cluster Autoscaler 與 Karpenter

| 面向 | Cluster Autoscaler | Karpenter |
| --- | --- | --- |
| 擴展單位 | 預先定義的 Node Group | 依 Pod 需求即時選擇機型 |
| 反應速度 | 較慢（透過 ASG／VMSS） | 較快（直接建立實例） |
| 成本最佳化 | 有限 | 整併（consolidation）、Spot 混用 |
| 支援 | 幾乎所有雲與 Cluster API | AWS、Azure（AKS NAP）等 |

> 📌 Node 擴縮必須搭配**正確的 request**：request 太大會浪費 Node，太小會讓 Node 超賣。也要搭配 PDB，否則縮減 Node 時可能一次驅逐太多 Pod。

---

### 6.5 Dynamic Resource Allocation（DRA）概覽

DRA（`resource.k8s.io/v1`，**1.34 GA**）是 GPU、FPGA、高速網卡等特殊裝置的新一代配置機制，取代以「數量」計算的 Device Plugin：

| 概念 | 說明 |
| --- | --- |
| `DeviceClass` | 管理員定義的裝置類別（例如「H100 GPU」） |
| `ResourceSlice` | 驅動程式回報每個 Node 上可用的裝置與屬性 |
| `ResourceClaim`／`ResourceClaimTemplate` | Pod 宣告需要的裝置，可用 CEL 依屬性篩選 |

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: single-gpu
  namespace: ml-prod
spec:
  spec:
    devices:
      requests:
        - name: gpu
          exactly:
            deviceClassName: gpu.example.com
---
apiVersion: v1
kind: Pod
metadata:
  name: trainer
  namespace: ml-prod
spec:
  resourceClaims:
    - name: gpu
      resourceClaimTemplateName: single-gpu
  containers:
    - name: trainer
      image: registry.example.com/ml/trainer:3.1.0
      resources:
        claims:
          - name: gpu
```

> 📌 1.35–1.37 DRA 持續擴充：Extended Resource 透過 DRA 處理、裝置污點與容忍、`numaNode` 標準屬性（1.37 GA）、管理員存取（1.36 GA）。一般企業在使用 GPU 工作負載時才需要深入；細節請參考各 GPU 廠商的 DRA 驅動文件。

---

### 6.6 💡 本章實務建議

1. **所有容器都必須設定 request 與 memory limit**，用 LimitRange 補預設值、用 Policy 強制（見 8.5）。
2. **Memory limit = request；CPU limit 依服務性質決定**，並把決策寫進平台規範。
3. **三種 Probe 分工明確**：Startup 等啟動、Liveness 只看自己、Readiness 看是否能接流量。
4. **關鍵服務**：至少 3 副本 + 跨區 `topologySpreadConstraints` + PDB（`maxUnavailable: 1`）+ 高 PriorityClass。
5. **擴縮策略**：HPA 以 CPU／RPS 為主，VPA 先開建議模式；事件驅動工作用 KEDA，1.37 起可評估 HPA 原生縮到 0。
6. **Node 擴縮**：雲端優先評估 Karpenter／EKS Auto Mode；地端用 Cluster API + Cluster Autoscaler。

---

## 7. kubectl 與日常操作

### 7.1 kubectl 常用指令

> 📌 **版本相容**：kubectl 支援與 API Server 相差 ±1 個 minor 版本（例如 kubectl 1.37 可操作 1.36–1.38）。管理多個叢集時，請依叢集版本準備對應的 kubectl。

#### 7.1.1 基本指令速查表

```bash
# ===== 環境與內容（context） =====
kubectl config get-contexts
kubectl config use-context prod-tpe-01
kubectl config set-context --current --namespace=order-prod

# ===== 查詢 =====
kubectl get all -n order-prod                      # 注意：all 不含 ConfigMap、Secret、Gateway 等
kubectl get pods -o wide
kubectl get pods -l app.kubernetes.io/name=order-service --show-labels
kubectl get deploy,svc,httproute -n order-prod
kubectl describe pod <pod-name>
kubectl api-resources --namespaced=true            # 列出所有資源類型
kubectl explain deployment.spec.strategy --recursive   # 查欄位說明（不用翻文件）

# ===== 建立與套用 =====
kubectl apply -f deployment.yaml
kubectl apply -f ./manifests/ --server-side --field-manager=platform-ci   # Server-Side Apply
kubectl diff -f deployment.yaml                    # 套用前先比對差異
kubectl create deployment nginx --image=nginx:1.30.5 --dry-run=client -o yaml > nginx.yaml

# ===== 刪除 =====
kubectl delete -f deployment.yaml
kubectl delete pod <pod-name>
kubectl delete pod <pod-name> --grace-period=0 --force   # 強制刪除（只在 Node 已失聯時使用）

# ===== 執行與除錯 =====
kubectl exec -it <pod-name> -c <container> -- sh
kubectl logs <pod-name> -f --since=10m
kubectl logs <pod-name> --previous                 # 前一次（崩潰前）的容器日誌
kubectl logs deploy/order-service --all-containers --prefix
kubectl cp <pod-name>:/tmp/heap.hprof ./heap.hprof  # 容器內需要有 tar
kubectl port-forward svc/order-service 8080:80

# ===== 資源管理 =====
kubectl scale deployment/order-service --replicas=5
kubectl set image deployment/order-service order-service=registry.example.com/ecommerce/order-service:1.4.3
kubectl patch deployment order-service --type=merge -p '{"spec":{"replicas":3}}'
kubectl label namespace order-prod gateway-access/public=true
kubectl annotate deployment order-service kubernetes.io/change-cause="CHG-20261001-02"

# ===== 事件與資源使用 =====
kubectl events -n order-prod --types=Warning       # 取代 get events --sort-by
kubectl events --for pod/<pod-name> --watch
kubectl top nodes
kubectl top pods -A --sort-by=memory
```

> ⚠️ **v2.0 更正**：v1.0 用 `kubectl run debug --image=busybox` 這類「另開一個 Pod」的方式除錯。這種 Pod 和問題 Pod 不在同一個網路與程序命名空間，很多問題看不到。本版改用 `kubectl debug`（見 [7.3](#73-kubectl-debug-與臨時容器)）。正式環境的 Namespace 通常也會以 Pod Security 禁止 root 除錯映像。

#### 7.1.2 輸出格式

```bash
# JSONPath
kubectl get pods -o jsonpath='{.items[*].metadata.name}'
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.phase}{"\n"}{end}'

# Custom Columns
kubectl get pods -o custom-columns=NAME:.metadata.name,NODE:.spec.nodeName,STATUS:.status.phase

# 排序與篩選
kubectl get pods --sort-by=.metadata.creationTimestamp
kubectl get pods --field-selector=status.phase!=Running -A

# KYAML（1.37 GA）：Kubernetes 的 YAML 方言，避免 Norway 問題與縮排歧義
kubectl get deploy order-service -o kyaml
```

> 🆕 **KYAML**：1.34 Alpha、1.35 Beta、**1.37 GA**。KYAML 是 YAML 的子集（任何 YAML 解析器都能讀），字串一律加引號、用 `{}`／`[]` 表示結構，不依賴縮排，可以避免 `NO` 被當成布林值、複製貼上縮排錯亂等問題。適合放在文件、Helm values 與 Code Review 中。

#### 7.1.3 Server-Side Apply（SSA）

| 面向 | Client-Side Apply（`kubectl apply`） | Server-Side Apply（`--server-side`） |
| --- | --- | --- |
| 合併邏輯 | 在 kubectl 端計算，依 `last-applied-configuration` 註解 | 在 API Server 計算，依 `managedFields` |
| 欄位擁有權 | 沒有 | 每個欄位有明確的 field manager，衝突時會報錯 |
| 大型物件（CRD） | 註解可能超過 256KB 上限 | 沒有這個問題 |
| 建議 | 既有流程 | **GitOps、控制器、CI 建議使用**（Argo CD、Flux、Helm 4 都支援） |

```bash
# 發生欄位衝突時，確認後才使用 --force-conflicts 接管欄位
kubectl apply --server-side --field-manager=platform-ci -f deployment.yaml
kubectl apply --server-side --field-manager=platform-ci --force-conflicts -f deployment.yaml
```

---

### 7.2 kubectl 使用者偏好：`.kuberc`（1.34 Beta）

`kuberc` 把**使用者偏好**（別名、預設參數、憑證外掛政策）和 kubeconfig（叢集連線資訊）分開。預設路徑 `~/.kube/kuberc`，也可以用 `--kuberc` 或 `KUBERC` 環境變數指定。

```yaml
# ~/.kube/kuberc
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
defaults:
  # kubectl apply 預設使用 Server-Side Apply
  - command: apply
    options:
      - name: server-side
        default: "true"
  # kubectl delete 預設要求互動確認
  - command: delete
    options:
      - name: interactive
        default: "true"
aliases:
  - name: getn
    command: get
    options:
      - name: output
        default: wide
# 只允許特定的 exec 憑證外掛（避免惡意 kubeconfig 執行任意程式）
credentialPluginPolicy: Allowlist
credentialPluginAllowlist:
  - name: kubelogin
  - name: aws-iam-authenticator
```

> 📌 **安全意義**：kubeconfig 可以透過 `exec` 欄位執行任意指令，拿到來路不明的 kubeconfig 等於執行未知程式。1.35 起 kuberc 支援 `credentialPluginPolicy`（Beta），企業可以統一發放 kuberc 限制可用的外掛。

---

### 7.3 kubectl debug 與臨時容器

```bash
# 1. 在執行中的 Pod 加入臨時容器（共享網路；--target 共享指定容器的程序命名空間）
kubectl debug -it pod/order-service-7d9f-abcde -n order-prod \
  --image=nicolaka/netshoot:v0.16 --target=order-service --profile=restricted

# 2. 複製一份 Pod 來除錯（不影響原 Pod），可同時替換映像或指令
kubectl debug pod/order-service-7d9f-abcde -n order-prod -it \
  --copy-to=order-debug --container=order-service -- sh

# 3. Node 除錯：在 Node 上建立 Pod，主機根目錄掛在 /host
kubectl debug node/worker-12 -it --image=ubuntu:24.04 --profile=sysadmin
# 進入後：chroot /host 或直接查看 /host/var/log
```

| `--profile` | 用途 | 權限 |
| --- | --- | --- |
| `legacy` | 舊版行為（預設值，將被淘汰） | 不一致 |
| `general` | 一般用途 | 合理預設 |
| `baseline` | 符合 Pod Security baseline | 較嚴 |
| `restricted` | 符合 Pod Security restricted | 最嚴，適合正式環境應用 Namespace |
| `netadmin` | 網路除錯（`NET_ADMIN`、`NET_RAW`） | 較高 |
| `sysadmin` | Node 層級除錯（特權） | 最高，只給平台管理員 |

> ⚠️ **v2.0 更正**：v1.0 標示 `--copy-to`「Kubernetes 1.25+」。臨時容器在 1.25 GA，但 `--profile` 才是控制權限的關鍵。建議在團隊規範中明確指定 profile，並以 RBAC 控管 `pods/ephemeralcontainers` 子資源。官方部落格〈Securing Production Debugging in Kubernetes〉（2026-03）建議：透過存取代理（access broker）核發短效、綁定身分的憑證，以 just-in-time 方式開放除錯權限，並同時保留閘道日誌與 Kubernetes 稽核日誌。

---

### 7.4 Deployment 發佈流程

```mermaid
flowchart TD
    A["CI 建置並掃描映像"] --> B["更新 Git 中的映像 tag"]
    B --> C["Argo CD / Flux 同步<br/>或 kubectl apply --server-side"]
    C --> D{"kubectl rollout status<br/>是否在 progressDeadline 內完成？"}
    D -->|成功| E["觀察 SLO 指標 15–30 分鐘"]
    D -->|失敗| F["檢查 Events、Pod 狀態、日誌"]
    E --> G{"錯誤率 / 延遲是否正常？"}
    G -->|正常| H["完成，關閉變更單"]
    G -->|異常| I["回滾：Git revert 或 rollout undo"]
    F --> I
```

```bash
# 1. 更新映像（GitOps 情境下改 Git，以下為手動流程）
kubectl set image deployment/order-service \
  order-service=registry.example.com/ecommerce/order-service:1.4.3 -n order-prod

# 2. 記錄變更原因（rollout history 的 CHANGE-CAUSE 欄位）
kubectl annotate deployment/order-service -n order-prod --overwrite \
  kubernetes.io/change-cause="1.4.3: fix tax rounding (CHG-20261001-02)"

# 3. 觀察發佈狀態（超過 progressDeadlineSeconds 會回傳非 0）
kubectl rollout status deployment/order-service -n order-prod --timeout=10m

# 4. 查看發佈歷史
kubectl rollout history deployment/order-service -n order-prod
kubectl rollout history deployment/order-service -n order-prod --revision=5

# 5. 暫停／恢復（一次修改多項設定時避免觸發多次滾動）
kubectl rollout pause deployment/order-service -n order-prod
kubectl rollout resume deployment/order-service -n order-prod

# 6. 重新啟動所有 Pod（例如 Secret 已更新）
kubectl rollout restart deployment/order-service -n order-prod
```

> ⚠️ **關於 `--record`**：舊文件常用 `kubectl set image ... --record` 記錄變更原因。這個旗標**已棄用**（kubectl 1.37 執行時會提示 `--record will be removed in the future`），而且記錄的是整行指令，可能包含敏感參數。請改用 `kubernetes.io/change-cause` 註解，GitOps 環境則以 Git commit 作為變更紀錄。

---

### 7.5 滾動更新與回滾

#### 7.5.1 滾動更新參數

```yaml
spec:
  minReadySeconds: 10          # 新 Pod Ready 後至少穩定 10 秒才算可用
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%            # 預設值：最多多出 25%
      maxUnavailable: 0        # 線上服務建議 0，確保容量不下降
```

| 情境 | maxSurge | maxUnavailable | 說明 |
| --- | --- | --- | --- |
| 線上服務（預設建議） | 25% 或 1 | 0 | 容量不下降，需要額外資源 |
| 資源緊張 | 0 | 1 | 不需額外資源，但容量暫時下降 |
| 大規模快速更新 | 50% | 0 | 需要大量額外資源 |
| 不允許新舊版本並存 | — | — | 改用 `type: Recreate`（會中斷服務） |

#### 7.5.2 回滾

```bash
# 回滾到上一版
kubectl rollout undo deployment/order-service -n order-prod

# 回滾到指定版本
kubectl rollout undo deployment/order-service -n order-prod --to-revision=4
```

> 📌 **GitOps 環境的回滾**：用 `kubectl rollout undo` 回滾後，Git 仍是新版，Argo CD／Flux 會在下次同步時「再把新版套回來」。正確做法是 **Git revert**，或先暫停自動同步再回滾。

---

### 7.6 進階發布策略：藍綠與金絲雀

| 策略 | 做法 | 優點 | 缺點 | 工具 |
| --- | --- | --- | --- | --- |
| 滾動更新 | 逐步替換 Pod | 內建、簡單 | 新舊版本並存、回滾較慢 | Deployment |
| 藍綠部署 | 兩套完整環境，切換流量 | 切換與回滾瞬間完成 | 資源加倍 | Service selector、Gateway API、Argo Rollouts |
| 金絲雀 | 小比例流量先到新版 | 風險最小，可依指標自動判斷 | 需要流量切分能力 | Gateway API 權重、Argo Rollouts、Flagger |

#### 7.6.1 以 Service selector 實作藍綠部署

```yaml
# Blue（目前版本）與 Green（新版本）各一個 Deployment，label 加上 track
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-green
  namespace: web-prod
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: myapp
      track: green
  template:
    metadata:
      labels:
        app.kubernetes.io/name: myapp
        track: green
    spec:
      containers:
        - name: app
          image: registry.example.com/web/myapp:2.0.0
---
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: web-prod
spec:
  selector:
    app.kubernetes.io/name: myapp
    track: blue          # 驗證 green 後改成 green 即完成切換；改回 blue 即回滾
  ports:
    - port: 80
      targetPort: 8080
```

#### 7.6.2 以 Argo Rollouts 自動化金絲雀

Argo Rollouts（v1.10.0）以 `Rollout` 資源取代 Deployment，可整合 Gateway API 的權重分流與 Prometheus 指標自動判斷（Gateway API 外掛需先在 `argo-rollouts-config` ConfigMap 註冊）：

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: order-service
  namespace: order-prod
spec:
  replicas: 5
  selector:
    matchLabels:
      app.kubernetes.io/name: order-service
  template:
    metadata:
      labels:
        app.kubernetes.io/name: order-service
    spec:
      containers:
        - name: order-service
          image: registry.example.com/ecommerce/order-service:1.4.3
  strategy:
    canary:
      canaryService: order-service-canary
      stableService: order-service
      trafficRouting:
        plugins:
          argoproj-labs/gatewayAPI:          # Gateway API 流量外掛
            httpRoute: order-api
            namespace: order-prod
      steps:
        - setWeight: 10
        - pause: {duration: 10m}
        - analysis:
            templates:
              - templateName: success-rate   # 以 Prometheus 查詢錯誤率，失敗自動回滾
        - setWeight: 50
        - pause: {duration: 10m}
```

---

### 7.7 kubectl 外掛與輔助工具

| 工具 | 用途 |
| --- | --- |
| **krew** | kubectl 外掛管理器 |
| **kubectx／kubens** | 快速切換 context 與 namespace |
| **stern** | 同時追蹤多個 Pod 的日誌 |
| **k9s** | 終端機 UI |
| **Headlamp** | 圖形化管理介面（Kubernetes SIG UI 專案，取代已封存的 Kubernetes Dashboard） |
| **kubelogin** | OIDC 登入（見 8.1） |

---

### 7.8 💡 本章實務建議

1. **正式環境以 GitOps 為主，kubectl 主要用於查詢與除錯**；寫入權限只給 CI 與值班人員，並全程稽核。
2. **統一發放 `kuberc`**：預設 Server-Side Apply、刪除需確認、限制憑證外掛。
3. **除錯一律用 `kubectl debug` 並指定 `--profile`**；Node 除錯權限只給平台管理員。
4. **以 `kubernetes.io/change-cause` 或 Git commit 記錄變更**，停止使用已棄用的 `--record`。
5. **線上服務滾動更新使用 `maxUnavailable: 0` + `minReadySeconds`**；高風險變更採用金絲雀 + 指標自動判斷。

---

## 8. 安全強化

> 🆕 **v2.0 新增章節**：v1.0 的安全內容分散在 RBAC、Secret 與最佳實踐章節，深度不足。本章依「4C」模型（Cloud → Cluster → Container → Code）整理 Kubernetes 1.37 的完整安全控制。

```mermaid
flowchart LR
    subgraph Req["每個 API 請求的處理順序"]
        A["認證<br/>Authentication"] --> B["授權<br/>Authorization（RBAC / Node / Webhook）"]
        B --> C["Mutating Admission<br/>MAP / Webhook"]
        C --> D["Schema 驗證"]
        D --> E["Validating Admission<br/>VAP / PSA / Webhook"]
        E --> F["寫入 etcd<br/>（KMS v2 加密）"]
    end
```

### 8.1 認證（Authentication）

#### 8.1.1 認證方式比較

| 方式 | 適用對象 | 建議 |
| --- | --- | --- |
| X.509 用戶端憑證（admin.conf） | 叢集建立、緊急存取 | **只作為 break-glass**；憑證無法撤銷，鎖進保險庫 |
| **OIDC（結構化認證設定）** | 人員 | **人員登入的標準做法**，串接企業 IdP（Entra ID、Keycloak、Okta） |
| ServiceAccount Token | Pod 內的應用、CI | 使用短效的 bound token（8.3） |
| 雲端 IAM | Managed K8s | EKS Access Entries、GKE IAM、AKS Entra ID |
| 靜態 Token 檔案 | — | **禁止使用** |

#### 8.1.2 結構化認證設定（Structured Authentication Configuration，1.34 GA）

取代過去的 `--oidc-*` 旗標，支援**多個 Issuer**、CEL 規則、動態重新載入：

```yaml
# /etc/kubernetes/auth/authentication-config.yaml
# kube-apiserver 啟動參數：--authentication-config=/etc/kubernetes/auth/authentication-config.yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AuthenticationConfiguration
jwt:
  - issuer:
      url: https://sso.example.com/realms/corp
      audiences:
        - kubernetes-prod
      certificateAuthority: |
        -----BEGIN CERTIFICATE-----
        ...企業 CA...
        -----END CERTIFICATE-----
    claimValidationRules:
      - expression: "claims.email_verified == true"
        message: "email 必須經過驗證"
    claimMappings:
      username:
        expression: "'oidc:' + claims.email"
      groups:
        expression: "claims.groups.map(g, 'oidc:' + g)"
      uid:
        claim: sub
    userValidationRules:
      - expression: "!user.username.startsWith('oidc:system:')"
        message: "不得冒用 system: 前綴"
anonymous:
  enabled: true
  conditions:                    # 1.34 GA：只允許健康檢查端點匿名存取
    - path: /livez
    - path: /readyz
    - path: /healthz
```

```bash
# 使用者端：kubelogin（int128/kubelogin）自動取得並更新 OIDC Token
kubectl oidc-login setup --oidc-issuer-url=https://sso.example.com/realms/corp --oidc-client-id=kubernetes-prod
```

> 📌 **1.34 差異**：結構化認證 1.30–1.33 為 Beta、1.34 GA；1.34 以上請使用 `apiserver.config.k8s.io/v1`。舊的 `--oidc-*` 旗標仍可用，但不能和 `--authentication-config` 同時使用。

---

### 8.2 RBAC 權限控管

#### 8.2.1 RBAC 架構

```mermaid
flowchart LR
    S["Subject<br/>User / Group / ServiceAccount"] --> B["RoleBinding（Namespace）<br/>ClusterRoleBinding（叢集）"]
    R["Role（Namespace）<br/>ClusterRole（叢集或可重用）"] --> B
    B --> RES["Resources + Verbs<br/>pods: get, list, watch"]
```

| 組合 | 權限範圍 | 用途 |
| --- | --- | --- |
| Role + RoleBinding | 單一 Namespace | 團隊在自己 Namespace 的權限 |
| ClusterRole + RoleBinding | 單一 Namespace（重用 ClusterRole 定義） | **建議**：用內建 `view`／`edit`／`admin` 綁到各 Namespace |
| ClusterRole + ClusterRoleBinding | 整個叢集 | 平台管理員、叢集層級元件 |

#### 8.2.2 RBAC 設定範例

```yaml
# 以內建 ClusterRole "edit" 授權團隊群組（來自 OIDC groups claim）
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: order-team-edit
  namespace: order-dev
subjects:
  - kind: Group
    name: "oidc:order-developers"
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: edit
  apiGroup: rbac.authorization.k8s.io
---
# 正式環境只給唯讀 + 查看日誌
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: prod-readonly-with-logs
  namespace: order-prod
rules:
  - apiGroups: [""]
    resources: ["pods", "pods/log", "services", "configmaps", "events"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["apps"]
    resources: ["deployments", "replicasets", "statefulsets"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["gateway.networking.k8s.io"]
    resources: ["httproutes", "grpcroutes"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: order-team-prod-readonly
  namespace: order-prod
subjects:
  - kind: Group
    name: "oidc:order-developers"
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: prod-readonly-with-logs
  apiGroup: rbac.authorization.k8s.io
---
# 應用程式的 ServiceAccount 與對應權限（只讀取自己的 ConfigMap）
apiVersion: v1
kind: ServiceAccount
metadata:
  name: order-service
  namespace: order-prod
automountServiceAccountToken: false
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: order-service-config-reader
  namespace: order-prod
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    resourceNames: ["order-service-config"]
    verbs: ["get", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: order-service-config-reader
  namespace: order-prod
subjects:
  - kind: ServiceAccount
    name: order-service
    namespace: order-prod
roleRef:
  kind: Role
  name: order-service-config-reader
  apiGroup: rbac.authorization.k8s.io
```

> ⚠️ **v2.0 更正**：v1.0 的 RoleBinding 引用了不存在的 Role `service-role`；另一個 ClusterRole 範例用 `resources: ["*"]` 授予 core 群組所有資源的唯讀權限，**這會包含 Secret**（等同可讀取所有密碼）。唯讀需求請使用內建的 `view` ClusterRole（預設不含 Secret），或明確列出資源。

#### 8.2.3 高風險權限清單

| 權限 | 風險 |
| --- | --- |
| Secret 的 `get`／`list`／`watch` | 讀取所有機密；`list` 也會回傳內容 |
| `pods/exec`、`pods/attach`、`pods/ephemeralcontainers` | 在容器內執行任意指令 |
| 建立 Pod／Deployment（任何工作負載） | 可以掛載同 Namespace 的任何 Secret、使用任何 ServiceAccount |
| `nodes/proxy`（含 **get**） | 可以透過 kubelet 在 Node 上任何容器執行指令 |
| `escalate`、`bind`、`impersonate` | 權限提升 |
| 修改 `validatingwebhookconfigurations`／`mutatingwebhookconfigurations`／admission policy | 關閉安全控管 |
| `serviceaccounts/token` 的 `create` | 為任意 SA 簽發 Token |
| `*` 萬用字元 | 未來新增的資源也會被授權 |

#### 8.2.4 1.34–1.37 的授權改進

- **細粒度 kubelet 授權（1.36 GA）**：監控工具只需要 `nodes/metrics`、`nodes/stats`，以及新的 `nodes/healthz`、`nodes/pods`、`nodes/configz` 等子資源，**不再需要危險的 `nodes/proxy`**。請檢查既有的監控 ClusterRole 並移除 `nodes/proxy`。
- **依 selector 授權（1.34 GA）**：Webhook 授權器可以依 label／field selector 決定，例如只允許 kubelet `list` 自己 Node 上的 Pod。
- **受限的身分代理（Constrained Impersonation，1.36 Beta）**：代理者需要兩種權限，`impersonate:user-info`（可以代理誰）加上 `impersonate-on:user-info:<verb>`（代理時能做什麼），取代過去「能代理就能做該使用者的所有事」的 `impersonate` 動詞。

```bash
# 權限檢查
kubectl auth can-i create deployments -n order-prod --as=jane@example.com
kubectl auth can-i --list -n order-prod --as=system:serviceaccount:order-prod:order-service
kubectl auth whoami          # 顯示目前的身分與群組（1.28 GA）
```

---

### 8.3 ServiceAccount 與 Token 安全

| 項目 | 建議 |
| --- | --- |
| Token 類型 | 使用 **bound service account token**（有期限、綁定 Pod、自動輪替），由 projected volume 提供 |
| 自動掛載 | 應用不需要呼叫 Kubernetes API 時，設定 `automountServiceAccountToken: false` |
| 舊式 Secret Token | 1.24 起不再自動建立；1.30 起會自動清理長期未使用的舊式 Token（`LegacyServiceAccountTokenCleanUp` GA） |
| CI／外部系統 | 用 `kubectl create token <sa> --duration=1h` 或 OIDC Workload Identity Federation，不要匯出長效 Token |
| 外部簽署（1.36 GA） | API Server 可以透過外部簽署服務（HSM／KMS）簽發 SA Token，私鑰不必放在 Control Plane 檔案系統 |
| 映像拉取（1.34 Beta） | kubelet 的 image credential provider 可以使用 Pod 的 SA Token 取得 Registry 憑證，取代 Node 層級的長效 `imagePullSecrets` |

```yaml
# 需要特定 audience 的短效 Token（例如給 Vault 驗證）
spec:
  serviceAccountName: order-service
  containers:
    - name: app
      image: registry.example.com/ecommerce/order-service:1.4.2
      volumeMounts:
        - name: vault-token
          mountPath: /var/run/secrets/vault
          readOnly: true
  volumes:
    - name: vault-token
      projected:
        sources:
          - serviceAccountToken:
              audience: vault
              expirationSeconds: 3600
              path: token
```

---

### 8.4 Pod Security Admission 與 securityContext

#### 8.4.1 Pod Security Standards 三個等級

| 等級 | 說明 | 適用 |
| --- | --- | --- |
| `privileged` | 不限制 | 系統元件（CNI、CSI、監控 Agent） |
| `baseline` | 禁止已知的權限提升（hostNetwork、privileged、hostPath 等） | 過渡期、第三方軟體 |
| `restricted` | 再加上必須非 root、drop ALL capabilities、seccomp RuntimeDefault、禁止 Probe `host` 欄位等 | **應用程式 Namespace 預設** |

Pod Security Admission（PSA）以 Namespace 標籤啟用，有三種模式：

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: order-prod
  labels:
    pod-security.kubernetes.io/enforce: restricted      # 違反即拒絕
    pod-security.kubernetes.io/enforce-version: v1.37   # 固定版本，升級後再調整
    pod-security.kubernetes.io/audit: restricted        # 記錄到 audit log
    pod-security.kubernetes.io/warn: restricted         # kubectl 顯示警告
```

```bash
# 套用前先模擬：哪些既有 Pod 會違反 restricted
kubectl label --dry-run=server --overwrite ns order-prod pod-security.kubernetes.io/enforce=restricted
```

> ⚠️ **PodSecurityPolicy（PSP）已於 1.25 移除**。仍在參考 PSP 文件的團隊請改用 PSA，加上 VAP／Kyverno 處理 PSA 無法涵蓋的客製規則。

#### 8.4.2 符合 restricted 的 securityContext 範本

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 10001
    runAsGroup: 10001
    fsGroup: 10001
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: registry.example.com/app:2.0.1
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
        appArmorProfile:              # 1.31 GA，取代舊的 annotation
          type: RuntimeDefault
```

#### 8.4.3 User Namespaces（1.36 GA）

設定 `hostUsers: false` 後，容器內的 root（UID 0）會對應到主機上的非特權 UID。即使容器被突破，在主機上也沒有 root 權限，可以緩解多數容器逃逸漏洞：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: isolated-app
spec:
  hostUsers: false          # 啟用 user namespace
  containers:
    - name: app
      image: registry.example.com/legacy-app-needs-root:3.2.0
```

> 📌 需要 Linux 核心 6.3 以上、支援 idmap mount 的檔案系統，以及 containerd 2.x 或 CRI-O。適合**必須以 root 執行的舊應用**、多租戶與 CI build 環境。1.34／1.35 為 Beta（預設開啟）。

---

### 8.5 Admission 控制：Validating／MutatingAdmissionPolicy 與政策引擎

| 方案 | 類型 | 優點 | 缺點 |
| --- | --- | --- | --- |
| **ValidatingAdmissionPolicy（VAP）** | 內建（1.30 GA），CEL | 不需要額外元件、在 API Server 內執行、延遲低 | 只能驗證，無法查詢其他物件 |
| **MutatingAdmissionPolicy（MAP）** | 內建（1.36 GA），CEL | 內建的 mutation，取代簡單的 Webhook | 1.36 才 GA |
| **Kyverno**（1.19） | 外部，YAML／CEL | 驗證、變更、產生、映像簽章驗證、報表 | 需要維運 Webhook |
| **OPA Gatekeeper**（3.23） | 外部，Rego | 成熟、跨平台政策語言 | 學習曲線高 |

#### 8.5.1 ValidatingAdmissionPolicy 範例：禁止 latest 標籤、要求資源設定

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicy
metadata:
  name: workload-baseline.example.com
spec:
  failurePolicy: Fail
  matchConstraints:
    resourceRules:
      - apiGroups: ["apps"]
        apiVersions: ["v1"]
        operations: ["CREATE", "UPDATE"]
        resources: ["deployments", "statefulsets", "daemonsets"]
  validations:
    - expression: >-
        object.spec.template.spec.containers.all(c,
          !c.image.endsWith(':latest') && c.image.contains(':'))
      message: "映像必須指定明確版本，不可使用 latest"
    - expression: >-
        object.spec.template.spec.containers.all(c,
          has(c.resources.requests) && has(c.resources.limits) &&
          'memory' in c.resources.limits)
      message: "每個容器都必須設定 requests 與 memory limit"
    - expression: >-
        object.spec.template.spec.containers.all(c,
          c.image.startsWith('registry.example.com/'))
      message: "只能使用企業內部 Registry 的映像"
---
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicyBinding
metadata:
  name: workload-baseline-binding
spec:
  policyName: workload-baseline.example.com
  validationActions: ["Deny", "Audit"]      # 導入初期可先用 ["Warn", "Audit"]
  matchResources:
    namespaceSelector:
      matchLabels:
        example.com/tier: application
```

#### 8.5.2 MutatingAdmissionPolicy 範例：自動補上預設標籤

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingAdmissionPolicy
metadata:
  name: default-team-label.example.com
spec:
  matchConstraints:
    resourceRules:
      - apiGroups: [""]
        apiVersions: ["v1"]
        operations: ["CREATE"]
        resources: ["pods"]
  matchConditions:
    - name: missing-team-label
      expression: "!has(object.metadata.labels) || !('example.com/team' in object.metadata.labels)"
  failurePolicy: Fail
  reinvocationPolicy: IfNeeded
  mutations:
    - patchType: ApplyConfiguration
      applyConfiguration:
        expression: >
          Object{
            metadata: Object.metadata{
              labels: {"example.com/team": namespaceObject.metadata.labels[?"example.com/team"].orValue("unknown")}
            }
          }
---
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingAdmissionPolicyBinding
metadata:
  name: default-team-label-binding
spec:
  policyName: default-team-label.example.com
```

> 🆕 **1.37 Beta：以檔案設定 Admission 政策**（Manifest-based admission control，`ManifestBasedAdmissionControlConfig` 1.37 起預設開啟）：在 `--admission-control-config-file` 指定的 AdmissionConfiguration 中設定 `staticManifestsDir`，API Server 會從磁碟載入 VAP／MAP 與 Webhook 設定。這些政策從 API Server 啟動就生效、不依賴 etcd，也能保護 API 中的 admission 資源不被修改，適合作為「平台底線政策」。
>
> 📌 **1.34／1.35 差異**：MAP 在 1.34–1.35 是 Beta（`admissionregistration.k8s.io/v1beta1`），需要開啟 Feature Gate 與 API；1.34／1.35 叢集請先用 Kyverno 實作 mutation。

---

### 8.6 Secret 靜態加密：KMS v2

```yaml
# /etc/kubernetes/enc/encryption-config.yaml
# kube-apiserver：--encryption-provider-config=/etc/kubernetes/enc/encryption-config.yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
      - configmaps            # 依資料分類決定是否加密
    providers:
      - kms:
          apiVersion: v2       # KMS v2（1.29 GA）：DEK 快取、效能佳、支援金鑰輪替
          name: corp-hsm
          endpoint: unix:///var/run/kmsplugin/socket.sock
          timeout: 3s
      - identity: {}           # 讀取尚未加密的舊資料用；全部重寫後可移除
```

```bash
# 啟用加密後，把既有 Secret 全部重寫一次，讓它們以新金鑰加密
kubectl get secrets -A -o json | kubectl replace -f -

# 驗證：直接讀 etcd，內容應以 k8s:enc:kms:v2: 開頭，而不是明文
sudo etcdctl get /registry/secrets/order-prod/order-db-credentials \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key | hexdump -C | head
```

> 📌 1.37 Beta 改善了「無法解密的資源」處理：KMS 金鑰遺失時，管理員可以找出並刪除無法解密的物件，避免整個資源類型的 list 失敗。**KMS 金鑰本身的備份與存取控制，是整個叢集資料安全的根基。**

---

### 8.7 工作負載身分：Pod 憑證與 ClusterTrustBundle（1.37 GA）

1.37 起，Kubernetes 原生支援為每個 Pod 簽發 X.509 憑證（mTLS 身分），不一定要靠 Service Mesh 或 cert-manager：

1. 平台團隊部署一個 **signer controller**，負責處理 `PodCertificateRequest`、簽發與輪替憑證，並維護 `ClusterTrustBundle`。
2. 工作負載透過 `podCertificate` projected volume 取得金鑰與憑證鏈，透過 `clusterTrustBundle` projected volume 取得信任錨點。

```yaml
spec:
  containers:
    - name: app
      image: registry.example.com/payment/api:5.0.0
      volumeMounts:
        - name: workload-identity
          mountPath: /var/run/identity
          readOnly: true
  volumes:
    - name: workload-identity
      projected:
        sources:
          - podCertificate:
              signerName: pki.example.com/workload
              keyType: ECDSAP256
              credentialBundlePath: credentialbundle.pem   # 私鑰 + 憑證鏈
          - clusterTrustBundle:
              signerName: pki.example.com/workload
              labelSelector:
                matchLabels:
                  pki.example.com/bundle: workload
              path: trust-bundle.pem
```

> 📌 `keyType` 可用值：`RSA3072`、`RSA4096`、`ECDSAP256`、`ECDSAP384`、`ECDSAP521`、`ED25519`。signer controller 需要自行實作或使用社群／廠商方案；在生態系成熟之前，cert-manager（v1.21）＋ csi-driver 或 Service Mesh 仍是主流做法。

---

### 8.8 網路安全進階：零信任與 Service Mesh

| 層次 | 做法 |
| --- | --- |
| L3/L4 隔離 | NetworkPolicy default-deny（見 [4.9](#49-networkpolicy-基礎)），Cilium／Calico 擴充 FQDN 與叢集層級政策 |
| 東西向加密 | Service Mesh mTLS（Istio ambient mode、Linkerd、Cilium mutual auth）或 Pod 憑證 |
| L7 授權 | Istio `AuthorizationPolicy`、Cilium L7 policy |
| 南北向 | Gateway API + WAF、雲端 LB 安全群組、`allowedRoutes` |
| Egress 控管 | Egress Gateway、FQDN 白名單，避免 Pod 任意連外 |

> 📌 Istio ambient mode（不需 sidecar）自 Istio 1.24 起 GA，顯著降低 Mesh 的資源與維運成本，是 2026 年新導入 Mesh 時優先評估的模式。

---

### 8.9 Audit Log（稽核日誌）

```yaml
# /etc/kubernetes/audit-policy.yaml（kubeadm 設定見 2.1.2）
apiVersion: audit.k8s.io/v1
kind: Policy
omitStages:
  - RequestReceived
rules:
  # 1. 不記錄高頻、低價值的請求
  - level: None
    users: ["system:kube-proxy"]
    verbs: ["watch"]
  - level: None
    nonResourceURLs: ["/healthz*", "/livez*", "/readyz*", "/version"]
  # 2. Secret、ConfigMap、Token 只記 Metadata（不能記錄內容）
  - level: Metadata
    resources:
      - group: ""
        resources: ["secrets", "configmaps", "serviceaccounts/token"]
  # 3. exec / attach / port-forward / 臨時容器一律記錄
  - level: RequestResponse
    resources:
      - group: ""
        resources: ["pods/exec", "pods/attach", "pods/portforward", "pods/ephemeralcontainers"]
  # 4. RBAC 與 Admission 設定變更記錄完整內容
  - level: RequestResponse
    resources:
      - group: "rbac.authorization.k8s.io"
      - group: "admissionregistration.k8s.io"
  # 5. 其餘寫入操作記錄 Request
  - level: Request
    verbs: ["create", "update", "patch", "delete", "deletecollection"]
  # 6. 其餘讀取只記 Metadata
  - level: Metadata
```

> 📌 稽核日誌要**送到叢集外**的 SIEM（不可只存在 Control Plane 本機），並依法規保留（金融業通常 1–7 年）。kube-apiserver 的 `--audit-log-maxage`、`--audit-log-maxbackup`、`--audit-log-maxsize` 控制本機輪替。

---

### 8.10 供應鏈安全

```mermaid
flowchart LR
    SRC["原始碼<br/>簽章 commit"] --> BUILD["CI 建置<br/>最小化基礎映像"]
    BUILD --> SCAN["掃描<br/>Trivy：漏洞、Secret、設定"]
    SCAN --> SBOM["產生 SBOM<br/>SPDX / CycloneDX"]
    SBOM --> SIGN["簽章與證明<br/>cosign / SLSA provenance"]
    SIGN --> REG["企業 Registry<br/>Harbor / ECR / ACR"]
    REG --> ADM["部署時驗證<br/>Kyverno verifyImages"]
    ADM --> RUN["執行期偵測<br/>Falco / Tetragon"]
```

| 控制點 | 工具（2026-09 版本） | 做法 |
| --- | --- | --- |
| 基礎映像 | distroless、Chainguard、UBI-micro | 不含 shell 與套件管理器 |
| 漏洞掃描 | Trivy v0.74.0 | CI 中 `--exit-code 1 --severity HIGH,CRITICAL`；Registry 定期重掃 |
| SBOM | Trivy、Syft | 隨映像以 OCI artifact 發佈 |
| 簽章 | cosign v3.1.3（Sigstore） | keyless（OIDC）或企業 KMS 金鑰 |
| 部署驗證 | Kyverno `verifyImages`、Sigstore policy-controller | 只允許已簽章、來自企業 Registry 的映像 |
| 以 digest 部署 | — | `image: repo@sha256:...`，tag 可以被覆蓋，digest 不行 |
| 執行期 | Falco、Tetragon | 偵測異常系統呼叫、可疑 shell |

```bash
# 簽章（keyless，CI 的 OIDC 身分）並驗證
cosign sign registry.example.com/ecommerce/order-service@sha256:<digest>
cosign verify registry.example.com/ecommerce/order-service@sha256:<digest> \
  --certificate-identity-regexp='^https://gitlab.example.com/ecommerce/order-service//.*' \
  --certificate-oidc-issuer=https://gitlab.example.com
```

```yaml
# Kyverno：只允許已簽章的企業映像
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-image-signature
spec:
  validationFailureAction: Enforce
  webhookTimeoutSeconds: 30
  rules:
    - name: verify-cosign
      match:
        any:
          - resources:
              kinds: ["Pod"]
      verifyImages:
        - imageReferences:
            - "registry.example.com/*"
          attestors:
            - entries:
                - keys:
                    kms: "awskms:///arn:aws:kms:ap-northeast-1:111122223333:key/cosign-signing"
```

> 📌 Kyverno 1.14 起推出以 CEL 為基礎的新政策類型（例如 `ImageValidatingPolicy`）。既有的 `ClusterPolicy` 仍然支援，新專案可依 Kyverno 版本選擇。

---

### 8.11 合規基準與安全檢查

| 基準／工具 | 用途 |
| --- | --- |
| **CIS Kubernetes Benchmark** | 業界最常用的設定基準；kube-bench（v0.16.0）自動檢查 |
| **NSA/CISA Kubernetes Hardening Guide** | 美國政府的強化指引 |
| **Pod Security Standards** | 工作負載層級基準（8.4） |
| Kubescape、Trivy Operator | 叢集內持續掃描設定與漏洞 |
| Falco | 執行期威脅偵測（CNCF 畢業專案） |

```bash
# 在 Control Plane 與 Worker 上執行 CIS 檢查
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/v0.16.0/job.yaml
kubectl logs job/kube-bench
```

---

### 8.12 💡 本章實務建議

1. **人員一律用 OIDC 登入**（結構化認證設定），admin.conf 只作為 break-glass 並納入金庫管理。
2. **RBAC 以群組授權**，使用內建 `view`／`edit`／`admin`；定期以 `kubectl auth can-i --list` 與工具（例如 rbac-tool）稽核高風險權限。
3. **監控工具移除 `nodes/proxy`**，改用 1.36 GA 的細粒度 kubelet 權限。
4. **應用 Namespace 一律 `restricted`**，必須 root 的舊系統優先改用 `hostUsers: false`。
5. **政策即程式碼**：基本規則用 VAP／MAP（不需外部元件），進階規則與映像驗證用 Kyverno；政策先 `Warn` 再 `Deny`。
6. **KMS v2 + 稽核日誌送外部 SIEM** 是金融業的最低要求。
7. **供應鏈**：掃描 → SBOM → 簽章 → 部署驗證 → 執行期偵測，五個控制點都要有。

---

## 9. 可觀測性：監控、日誌與追蹤

### 9.1 可觀測性架構總覽

```mermaid
flowchart LR
    subgraph K8s["Kubernetes Cluster"]
        APP["應用 Pod<br/>OTel SDK / /metrics / stdout"]
        KSM["kube-state-metrics"]
        NE["node-exporter"]
        KL["kubelet / cAdvisor<br/>/metrics/resource"]
        MS["metrics-server"]
        COL["OTel Collector / Alloy / Fluent Bit<br/>（DaemonSet + Gateway）"]
        PROM["Prometheus（Operator）"]
    end
    APP -- "metrics" --> PROM
    KSM --> PROM
    NE --> PROM
    KL --> PROM
    KL --> MS
    MS -- "metrics.k8s.io" --> HPA["HPA / kubectl top"]
    APP -- "logs（stdout → /var/log/pods）" --> COL
    APP -- "traces（OTLP）" --> COL
    PROM -- "remote write" --> LT["長期儲存<br/>Thanos / Mimir / VictoriaMetrics"]
    COL --> LOGS["日誌後端<br/>Elasticsearch / Loki / OpenSearch"]
    COL --> TR["追蹤後端<br/>Tempo / Jaeger / APM"]
    LT --> G["Grafana / Kibana"]
    LOGS --> G
    TR --> G
```

| 訊號 | 標準 | 建議工具（2026-09） |
| --- | --- | --- |
| 指標（Metrics） | Prometheus 格式、OTLP | Prometheus v3.15 + kube-prometheus-stack、Thanos／Mimir |
| 日誌（Logs） | stdout／stderr + 結構化 JSON | Fluent Bit v5.1、Grafana Alloy v1.20、OTel Collector → Elasticsearch／Loki v3.7 |
| 追蹤（Traces） | OpenTelemetry（OTLP） | OTel Operator v0.160、Tempo、Jaeger |
| 事件（Events） | Kubernetes Events | kubernetes-event-exporter、OTel `k8sobjects` receiver |
| 剖析（Profiles） | OTel Profiles | Pyroscope |

---

### 9.2 Prometheus 3 與 kube-prometheus-stack

#### 9.2.1 資源指標：metrics-server 與 metrics.k8s.io（1.37 GA）

```bash
# 安裝 metrics-server v0.9.0（kubectl top 與 HPA 的資料來源）
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.9.0/components.yaml

kubectl top nodes
kubectl top pods -A --containers
```

> 🆕 **1.37**：`metrics.k8s.io` 在 Beta 將近九年後**升級為 GA（`v1`）**；`v1beta1` 在過渡期仍可使用。metrics-server 只提供「現在」的 CPU／記憶體，**不是監控系統**，歷史資料與告警請用 Prometheus。

#### 9.2.2 安裝 kube-prometheus-stack

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install kps prometheus-community/kube-prometheus-stack --version 91.8.2 \
  -n monitoring --create-namespace -f kps-values.yaml
```

```yaml
# kps-values.yaml（重點設定）
prometheus:
  prometheusSpec:
    retention: 15d
    retentionSize: 80GB
    replicas: 2
    # 讓 Prometheus 選取所有 namespace 的 ServiceMonitor（不限 Helm release 標籤）
    serviceMonitorSelectorNilUsesHelmValues: false
    podMonitorSelectorNilUsesHelmValues: false
    ruleSelectorNilUsesHelmValues: false
    storageSpec:
      volumeClaimTemplate:
        spec:
          storageClassName: fast-ssd
          resources:
            requests:
              storage: 100Gi
    remoteWrite:
      - url: https://mimir.example.internal/api/v1/push
alertmanager:
  alertmanagerSpec:
    replicas: 3
grafana:
  enabled: true
  admin:
    existingSecret: grafana-admin
```

> 📌 **Prometheus 3 的主要變化**（相對 2.x）：新 UI、原生 OTLP 接收端點（`/api/v1/otlp/v1/metrics`，需以 `--web.enable-otlp-receiver` 啟用）、UTF-8 指標名稱、Remote Write 2.0、Native Histograms 穩定化。從 2.x 升級前請閱讀官方 migration guide（部分 PromQL 與設定行為有變）。

#### 9.2.3 以 ServiceMonitor 收集應用指標

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: order-service
  namespace: order-prod              # 和應用放同一個 namespace，由應用團隊維護
  labels:
    app.kubernetes.io/name: order-service
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: order-service
  endpoints:
    - port: http                     # Service 的具名埠
      path: /actuator/prometheus
      interval: 30s
      scrapeTimeout: 10s
```

#### 9.2.4 Kubernetes 必看指標與告警

| 類別 | 指標／告警 | 意義 |
| --- | --- | --- |
| Control Plane | `apiserver_request_duration_seconds`、`apiserver_request_total{code=~"5.."}` | API 延遲與錯誤率 |
| etcd | `etcd_disk_wal_fsync_duration_seconds`（p99 < 10ms）、`etcd_server_has_leader`、`etcd_mvcc_db_total_size_in_bytes` | 磁碟延遲、Leader、資料庫大小（預設配額 2 GiB，建議設到 8 GiB 並監控） |
| Node | `KubeNodeNotReady`、`NodeFilesystemAlmostOutOfSpace`、`kube_node_status_condition{condition="MemoryPressure"}` | Node 健康 |
| 工作負載 | `KubePodCrashLooping`、`KubeDeploymentReplicasMismatch`、`kube_pod_container_status_last_terminated_reason{reason="OOMKilled"}` | 應用異常 |
| 資源 | `container_cpu_cfs_throttled_periods_total`、`KubeCPUOvercommit`、`KubeQuotaAlmostFull` | 節流與容量 |
| 憑證 | `apiserver_client_certificate_expiration_seconds`、cert-manager `certmanager_certificate_expiration_timestamp_seconds` | 憑證到期 |
| 棄用 API | `apiserver_requested_deprecated_apis` | 升級前檢查（見 11.4） |
| 節點壓力 | PSI 指標（1.36 GA，`container_pressure_*`） | CPU／記憶體／IO 壓力，比使用率更能反映爭用 |

> 🆕 **1.37 Beta：Native Histograms**：Kubernetes 元件可以同時輸出傳統與原生直方圖（需要 Prometheus 以支援的協定抓取），儲存效率更好、精度更高。**1.37 Beta：CRI 提供容器統計**（cAdvisor-less），容器與 Pod 指標逐步改由 Container Runtime 直接提供。

---

### 9.3 日誌收集

#### 9.3.1 日誌收集架構

Kubernetes 不負責儲存日誌。容器寫到 stdout／stderr，Container Runtime 寫入 Node 的 `/var/log/pods/<ns>_<pod>_<uid>/<container>/N.log`（`/var/log/containers/` 是指向它的符號連結），再由 DaemonSet 收集器轉送到後端。

| 收集器 | 特色 | 建議 |
| --- | --- | --- |
| **Fluent Bit**（v5.1） | C 語言、資源占用低、CNCF 畢業 | 通用首選 |
| **Grafana Alloy**（v1.20） | OTel Collector 發行版，整合 Loki／Prometheus／Tempo | 使用 Grafana 生態系 |
| **OTel Collector**（filelog receiver） | 統一 metrics／logs／traces | 以 OpenTelemetry 為標準的組織 |
| Fluentd | Ruby、外掛豐富 | 既有系統維持，新系統改用 Fluent Bit |
| ~~Promtail~~ | 已於 2026 年初 EOL | 遷移到 Alloy |

#### 9.3.2 Fluent Bit 部署（Helm）

```bash
helm repo add fluent https://fluent.github.io/helm-charts
helm install fluent-bit fluent/fluent-bit -n logging --create-namespace -f fluent-bit-values.yaml
```

```yaml
# fluent-bit-values.yaml（chart 的 config 區塊使用 classic 設定格式）
image:
  tag: "5.1.2"
config:
  inputs: |
    [INPUT]
        Name              tail
        Path              /var/log/containers/*.log
        Exclude_Path      /var/log/containers/fluent-bit*
        multiline.parser  cri
        Tag               kube.*
        Mem_Buf_Limit     50MB
        Skip_Long_Lines   On
        DB                /var/fluent-bit/state/flb_kube.db
  filters: |
    [FILTER]
        Name                kubernetes
        Match               kube.*
        Merge_Log           On
        Keep_Log            Off
        K8S-Logging.Parser  On
        K8S-Logging.Exclude On
  outputs: |
    [OUTPUT]
        Name            es
        Match           kube.*
        Host            es.logging.example.internal
        Port            9200
        tls             On
        HTTP_User       ${ES_USER}
        HTTP_Passwd     ${ES_PASSWORD}
        Logstash_Format On
        Logstash_Prefix k8s-logs
        Suppress_Type_Name On
envFrom:
  - secretRef:
      name: fluent-bit-es-credentials
```

> ⚠️ **v2.0 更正**：v1.0 的 Fluent Bit DaemonSet 掛載 `/var/lib/docker/containers`、使用 `fluent/fluent-bit:latest`。dockershim 已於 1.24 移除，containerd／CRI-O 的日誌在 `/var/log/pods`，格式是 **CRI 格式**（要用 `cri` multiline parser），不是 Docker JSON。本版改用官方 Helm chart，並固定版本。

#### 9.3.3 應用程式日誌建議（結構化 JSON）

```json
{
  "@timestamp": "2026-10-01T10:15:30.123+08:00",
  "log.level": "INFO",
  "service.name": "order-service",
  "service.version": "1.4.2",
  "trace.id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span.id": "00f067aa0ba902b7",
  "message": "Order created",
  "order.id": "ORD-12345",
  "user.id": "USR-67890"
}
```

| 原則 | 說明 |
| --- | --- |
| 寫到 stdout／stderr | 不要寫入容器內檔案（除非搭配 sidecar 轉送） |
| 一行一筆 JSON | 避免多行堆疊追蹤被拆散；Spring Boot 3.4+ 內建 `logging.structured.format.console=ecs` |
| 欄位命名採用標準 | ECS 或 OpenTelemetry Semantic Conventions，方便跨系統查詢 |
| 帶 trace／span ID | 讓日誌和追蹤可以互相跳轉 |
| 不記錄個資與機密 | 身分證號、卡號、密碼、Token 要遮罩 |

> ⚠️ **v2.0 更正**：v1.0 的日誌範例用 ` ```java ` 標示 JSON 內容，造成語法標示錯誤；本版改為 ` ```json `，並採用 ECS／OTel 欄位命名。

#### 9.3.4 Node 日誌輪替

kubelet 依 `containerLogMaxSize`（預設 10Mi）與 `containerLogMaxFiles`（預設 5）輪替容器日誌。高流量服務若日誌量大，請在收集器跟上的前提下調高，或改善應用日誌量，否則收集器可能來不及讀取就被輪替掉。

---

### 9.4 分散式追蹤與 OpenTelemetry

```yaml
# OpenTelemetry Operator：自動注入 Java Agent（Instrumentation CR）
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
metadata:
  name: java-auto
  namespace: order-prod
spec:
  exporter:
    endpoint: http://otel-collector.observability:4318
  propagators: [tracecontext, baggage]
  sampler:
    type: parentbased_traceidratio
    argument: "0.1"            # 取樣 10%
---
# 在 Pod template 加上註解即可注入
# metadata:
#   annotations:
#     instrumentation.opentelemetry.io/inject-java: "true"
```

| 元件 | 角色 |
| --- | --- |
| OTel SDK／Agent | 在應用中產生 span |
| OTel Collector（Agent 模式，DaemonSet） | 就近接收、加上 Kubernetes 中繼資料（`k8sattributes` processor） |
| OTel Collector（Gateway 模式，Deployment） | 集中取樣（tail sampling）、轉送到後端 |
| 後端 | Tempo、Jaeger、Elastic APM、商用 APM |

> 📌 Kubernetes 元件本身也支援 OpenTelemetry tracing（API Server 與 kubelet tracing 於 1.27 進入 Beta、**1.34 GA**），可以把 Control Plane 延遲納入同一套追蹤系統。

---

### 9.5 Kubernetes Events

Events 只在 etcd 保留約 1 小時（`--event-ttl` 預設 1h），而且是排查問題最重要的線索之一，**一定要匯出保存**：

```bash
kubectl events -A --types=Warning
kubectl events -n order-prod --for deployment/order-service
```

可以用 kubernetes-event-exporter，或 OTel Collector 的 `k8sobjects` receiver（watch `events`），把事件送到日誌後端並設定告警（例如 `FailedScheduling`、`BackOff`、`FailedMount`、`Evicted`）。

---

### 9.6 管理介面：Headlamp

> ⚠️ **v2.0 更正**：**Kubernetes Dashboard 已封存**（GitHub repo archived），官方建議改用 **Headlamp**（v0.45.0，Kubernetes SIG UI 專案）。Headlamp 支援 OIDC、外掛擴充（Flux、Cluster API、Kubeflow、Volcano 等），可以桌面版或叢集內部署。

```bash
helm repo add headlamp https://kubernetes-sigs.github.io/headlamp/
helm install headlamp headlamp/headlamp -n kube-system
```

---

### 9.7 💡 本章實務建議

1. **四大訊號都要有**：指標（Prometheus）、日誌（Fluent Bit／Alloy）、追蹤（OTel）、事件（Event exporter）。
2. **監控資料要離開叢集**：Prometheus remote write 與日誌後端應獨立於被監控的叢集，避免叢集故障時「連監控也一起看不到」。
3. **etcd 與 API Server 是 SLO 第一優先**：WAL fsync、Leader 變動、API 5xx 率、延遲都要告警。
4. **日誌統一 JSON + ECS／OTel 欄位**，並帶上 trace ID。
5. **以 OpenTelemetry 作為長期標準**，避免被單一 APM 廠商綁定。
6. **移除 Kubernetes Dashboard、Promtail 等已封存或 EOL 的元件**。

---

## 10. 維運與管理

### 10.1 Namespace 與多團隊隔離

#### 10.1.1 多租戶模型選擇

| 模型 | 隔離強度 | 成本 | 適用 |
| --- | --- | --- | --- |
| **Namespace 隔離**（軟性多租戶） | 低–中 | 低 | 同一組織內的多個團隊 |
| **Namespace + 專屬 Node Pool** | 中 | 中 | 有合規或效能隔離需求的團隊 |
| **虛擬叢集（vCluster v0.37）** | 中–高 | 中 | 團隊需要自己的 CRD／叢集管理權限 |
| **獨立叢集** | 高 | 高 | 不同法規等級（例如核心帳務 vs 行銷）、外部客戶 |

> 📌 **v2.0 補充**：多層級 Namespace 控制器 HNC（`kubernetes-sigs/hierarchical-namespaces`）已封存，不建議新導入。需要「租戶」抽象時可評估 Capsule（v0.14.6）或 vCluster。

#### 10.1.2 Namespace 設計策略

```mermaid
flowchart TB
    subgraph C["Kubernetes Cluster（prod-tpe-01）"]
        subgraph P["平台 Namespace"]
            KS["kube-system"]
            MON["monitoring"]
            LOG["logging"]
            EDGE["edge（Gateway）"]
        end
        subgraph A["應用 Namespace（<團隊>-<環境>）"]
            O["order-prod"]
            PAY["payment-prod"]
            U["user-prod"]
        end
    end
```

| 規則 | 說明 |
| --- | --- |
| 命名 | `<團隊或系統>-<環境>`，例如 `order-prod`；**正式與非正式環境不要放在同一叢集**（至少要不同 Node Pool） |
| 必備標籤 | `example.com/team`、`example.com/tier`、`example.com/data-class`、PSA 標籤 |
| 必備物件 | ResourceQuota、LimitRange、default-deny NetworkPolicy、RoleBinding |
| 建立方式 | 透過平台自助流程（GitOps 範本、Backstage、Capsule），不要手動建立 |

#### 10.1.3 Namespace 範本：Quota 與 LimitRange

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: order-prod
  labels:
    example.com/team: order
    example.com/tier: application
    example.com/data-class: confidential
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: v1.37
    gateway-access/public: "true"
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
  namespace: order-prod
spec:
  hard:
    requests.cpu: "40"
    requests.memory: 80Gi
    limits.memory: 80Gi
    pods: "200"
    services.loadbalancers: "0"          # 禁止自行建立 LoadBalancer，統一走 Gateway
    services.nodeports: "0"
    persistentvolumeclaims: "20"
    requests.storage: 2Ti
    count/secrets: "100"
    count/configmaps: "100"
---
# 限制高優先序 PriorityClass 的使用量
apiVersion: v1
kind: ResourceQuota
metadata:
  name: critical-priority-quota
  namespace: order-prod
spec:
  hard:
    pods: "30"
  scopeSelector:
    matchExpressions:
      - scopeName: PriorityClass
        operator: In
        values: ["business-critical"]
---
apiVersion: v1
kind: LimitRange
metadata:
  name: container-defaults
  namespace: order-prod
spec:
  limits:
    - type: Container
      defaultRequest:                    # 未設定 request 時的預設值
        cpu: 100m
        memory: 256Mi
      default:                           # 未設定 limit 時的預設值
        memory: 256Mi
      max:
        cpu: "4"
        memory: 8Gi
      min:
        cpu: 10m
        memory: 32Mi
    - type: PersistentVolumeClaim
      max:
        storage: 500Gi
```

> ⚠️ **v2.0 更正**：v1.0 的 LimitRange 設定 `default.cpu: 500m`，會讓所有沒設 CPU limit 的容器被套上 0.5 vCPU 上限，對 Java 等應用造成嚴重節流。本版依 [6.1.3](#613-qos-等級與-cpu-limit-的取捨) 的原則，預設只限制記憶體。

---

### 10.2 etcd 備份與還原

#### 10.2.1 備份

```bash
#!/usr/bin/env bash
# /usr/local/bin/etcd-backup.sh：在每台 Control Plane 以 systemd timer 或 CronJob 執行
set -euo pipefail
TS=$(date +%Y%m%d-%H%M)
SNAP=/var/backups/etcd/etcd-${HOSTNAME}-${TS}.db

etcdctl snapshot save "${SNAP}" \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

etcdutl snapshot status "${SNAP}" -w table          # 驗證快照
sha256sum "${SNAP}" > "${SNAP}.sha256"
# 加密後上傳到異地物件儲存（範例：S3 相容儲存，開啟物件鎖定）
aws s3 cp "${SNAP}" "s3://k8s-etcd-backup/prod-tpe-01/" --sse aws:kms
find /var/backups/etcd -name '*.db' -mtime +7 -delete
```

| 項目 | 建議 |
| --- | --- |
| 頻率 | 至少每日；變更頻繁的叢集每 1–4 小時 |
| 保存 | 本機 7 天 + 異地 30–90 天（依法規），物件鎖定防勒索 |
| 加密 | 快照內含所有 Secret（若未啟用 KMS 則是明文），**必須加密保存** |
| 驗證 | 每次備份執行 `etcdutl snapshot status`；每季做完整還原演練 |
| 一併備份 | `/etc/kubernetes/pki`（CA 金鑰）、kubeadm 設定檔、EncryptionConfiguration 與 KMS 金鑰資訊 |

#### 10.2.2 還原（kubeadm stacked etcd，單一成員示意）

```bash
# 1. 停止 Control Plane static Pod（移走 manifest）
sudo mkdir -p /etc/kubernetes/manifests.bak
sudo mv /etc/kubernetes/manifests/*.yaml /etc/kubernetes/manifests.bak/

# 2. 以 etcdutl 還原到新的資料目錄（etcd 3.6 起 etcdctl 已移除 snapshot restore）
sudo etcdutl snapshot restore /var/backups/etcd/etcd-cp1-20261001-0200.db \
  --name cp1 \
  --initial-cluster cp1=https://10.10.0.11:2380 \
  --initial-advertise-peer-urls https://10.10.0.11:2380 \
  --data-dir /var/lib/etcd-restore

# 3. 修改 etcd.yaml 的 hostPath 指向 /var/lib/etcd-restore（或替換原目錄）
sudo sed -i 's#/var/lib/etcd#/var/lib/etcd-restore#g' /etc/kubernetes/manifests.bak/etcd.yaml

# 4. 放回 manifest，kubelet 會重新啟動 Control Plane
sudo mv /etc/kubernetes/manifests.bak/*.yaml /etc/kubernetes/manifests/

# 5. 驗證
kubectl get nodes
kubectl get pods -A | grep -v Running
```

> ⚠️ **多成員叢集**：所有成員都要用**同一份快照**、各自的 `--name` 與相同的 `--initial-cluster` 還原，並同時啟動。還原後叢集狀態回到快照時間點，之後建立的資源會消失；控制器可能需要重新調和，Operator 管理的外部資源（雲端 LB、DNS）要逐一確認。
>
> 📌 **Managed K8s**：雲端代管叢集無法直接存取 etcd，請改用 Velero 等以 API 為基礎的備份（10.5）。

---

### 10.3 憑證管理

#### 10.3.1 kubeadm 叢集的憑證

| 憑證 | 預設效期 | 更新方式 |
| --- | --- | --- |
| CA（`ca.crt`、`etcd/ca.crt`、`front-proxy-ca.crt`） | 10 年（`caCertificateValidityPeriod`） | 手動輪替（高風險，需規劃） |
| API Server、etcd、front-proxy 等元件憑證 | 1 年（`certificateValidityPeriod`） | `kubeadm certs renew`；**每次 `kubeadm upgrade` 會自動更新** |
| kubelet 用戶端憑證 | 1 年 | kubelet 自動輪替（`rotateCertificates: true`，預設開啟） |
| kubelet 服務憑證 | 1 年 | `serverTLSBootstrap: true` + 核准 CSR |
| admin.conf／super-admin.conf | 1 年 | `kubeadm certs renew admin.conf` |

```bash
# 1. 檢查到期日
sudo kubeadm certs check-expiration

# 2. 更新所有元件憑證（每台 Control Plane 都要執行）
sudo kubeadm certs renew all

# 3. 重啟 Control Plane static Pod：暫時移走 manifest，等待約 20 秒後放回
sudo mkdir -p /tmp/k8s-manifests
sudo mv /etc/kubernetes/manifests/*.yaml /tmp/k8s-manifests/
sleep 20
sudo mv /tmp/k8s-manifests/*.yaml /etc/kubernetes/manifests/

# 4. 更新本機 kubeconfig
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config

# 5. 核准 kubelet 服務憑證 CSR（啟用 serverTLSBootstrap 時）
kubectl get csr --field-selector=spec.signerName=kubernetes.io/kubelet-serving
kubectl certificate approve <csr-name>
```

> ⚠️ **v2.0 更正**：v1.0 在 `kubeadm certs renew all` 之後只執行 `systemctl restart kubelet`。**重啟 kubelet 不會重啟 Control Plane 的 static Pod**，元件仍使用舊憑證，到期時一樣會中斷。官方做法是暫時移走 `/etc/kubernetes/manifests/` 中的檔案再放回。kubelet 服務憑證 CSR 也不會自動核准，建議部署自動核准控制器（例如 kubelet-csr-approver）並驗證 Node 身分。

#### 10.3.2 應用層憑證（cert-manager）

應用與 Gateway 的 TLS 憑證建議由 **cert-manager（v1.21）** 統一簽發與續期（企業內部 CA、Vault、ACME），詳見 [13.4](#134-cert-manager-憑證自動化)。

---

### 10.4 Cluster 容量與資源管理

#### 10.4.1 容量觀察指令

```bash
# Node 已分配資源（request 總和占 allocatable 比例）
kubectl describe nodes | grep -A 8 "Allocated resources"

# 實際使用量
kubectl top nodes
kubectl top pods -A --sort-by=cpu | head -20

# 各 Namespace 配額使用狀況
kubectl get resourcequota -A
kubectl describe resourcequota compute-quota -n order-prod
```

#### 10.4.2 Node 資源保留

kubelet 預設把 Node 的全部容量都給 Pod，Node 上的系統程序（kubelet、containerd、sshd）可能因此資源不足。請明確保留：

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
systemReserved:
  cpu: 500m
  memory: 1Gi
kubeReserved:
  cpu: 500m
  memory: 1Gi
evictionHard:
  memory.available: "500Mi"
  nodefs.available: "10%"
  imagefs.available: "15%"
```

#### 10.4.3 容量規劃建議

| 項目 | 建議 |
| --- | --- |
| 叢集 request 使用率 | 目標 60–75%；超過 80% 啟動擴容 |
| N+1 容量 | 任一 Node（或任一可用區）故障時，剩餘容量仍可容納所有關鍵 Pod |
| 升級餘裕 | 滾動升級 Node 時需要至少一台 Node 的空餘容量（`maxSurge`） |
| 超賣比例 | CPU request:實際使用可容許約 1.5–2 倍；記憶體不要超賣 |
| 檢討頻率 | 每月檢視 request 與實際使用的差距（VPA 建議、Kubecost／OpenCost） |

> ⚠️ **v2.0 更正**：v1.0 的容量表「系統元件 10–15%、突發 20–30%、建議可用 55–70%」沒有說明計算基準。本版改為以 **request 占 allocatable 的比例**作為衡量基準，並明確要求 N+1。

---

### 10.5 災難復原與 Velero

#### 10.5.1 DR 策略分級

| 等級 | 做法 | RPO | RTO |
| --- | --- | --- | --- |
| 備份還原 | Velero 備份到異地物件儲存，災難時重建叢集再還原 | 小時 | 小時–天 |
| 暖備援 | 第二叢集預先建好，GitOps 同步設定，資料以複寫方式同步 | 分鐘 | 分鐘–小時 |
| 雙活 | 兩地叢集同時服務，全域負載平衡（GSLB），資料層多活 | 接近 0 | 接近 0 |

> 📌 **GitOps 是 DR 的基礎**：所有 Kubernetes 物件都在 Git，重建叢集時只要指向同一個 repo 就能恢復「設定」；**真正困難的是「資料」**（PV、資料庫），需要依資料系統各自設計複寫與備份。

#### 10.5.2 Velero 備份

```bash
# 安裝 Velero v1.18.4（以 S3 相容儲存為例）
velero install \
  --provider aws \
  --plugins velero/velero-plugin-for-aws:v1.14.4 \
  --bucket k8s-velero-backup \
  --backup-location-config region=ap-northeast-1 \
  --secret-file ./velero-credentials \
  --use-node-agent \
  --default-volumes-to-fs-backup=false

# 每日 01:00 備份正式環境 namespace，保存 30 天，並建立 CSI 快照
velero schedule create prod-daily \
  --schedule "0 1 * * *" \
  --include-namespaces 'order-prod,payment-prod,user-prod' \
  --snapshot-volumes \
  --ttl 720h

# 還原到 DR 叢集（可改 namespace 名稱）
velero restore create --from-backup prod-daily-20261001010000 \
  --namespace-mappings order-prod:order-dr
```

> 📌 依 velero-plugin-for-aws 相容性表，Velero 1.18.x 對應外掛 v1.14.x。資料庫類工作負載要搭配 pre／post backup hook（例如先 `pg_backup_start`），或直接使用資料庫原生備份。

---

### 10.6 常見營運風險與因應

| 風險 | 影響 | 預防 | 偵測 |
| --- | --- | --- | --- |
| **etcd 故障或資料損壞** | 整個叢集無法運作 | 3／5 成員、SSD、定期快照 + 異地保存 | etcd 指標、備份成功告警 |
| **etcd 資料庫超過配額** | 叢集變唯讀（`mvcc: database space exceeded`） | 調高 `--quota-backend-bytes`、定期 defrag、避免大量 Event／大型 ConfigMap | `etcd_mvcc_db_total_size_in_bytes` |
| **憑證過期** | API Server 無法存取、Node NotReady | 每次升級自動更新、到期前 30 天告警 | `kubeadm certs check-expiration`、憑證指標 |
| **Node 故障** | Node 上的 Pod 中斷 | 多副本 + 拓撲分散 + PDB | `KubeNodeNotReady` |
| **資源耗盡** | 新 Pod Pending、Node 驅逐 | ResourceQuota、系統保留、Cluster Autoscaler | `FailedScheduling`、`Evicted` |
| **映像拉取失敗** | Pod 無法啟動 | 企業 Registry + 鏡像快取、固定 digest、拉取憑證輪替 | `ImagePullBackOff` 告警 |
| **版本落後** | 失去安全更新、雲端延長支援費 | 每年至少升級 2–3 個 minor 版本 | 版本盤點儀表板 |
| **Webhook 故障** | 所有相關 API 請求失敗 | Webhook 多副本、`failurePolicy` 與 `namespaceSelector` 排除 kube-system；優先使用 VAP／MAP | API Server `apiserver_admission_webhook_rejection_count` |
| **使用已退役元件** | 未修補漏洞 | 定期盤點（Ingress NGINX、Dashboard、Promtail、kube-dns） | 元件版本清單 |

---

### 10.7 💡 本章實務建議

1. **Namespace 以範本自助建立**，Quota、LimitRange、NetworkPolicy、RBAC、PSA 一次到位。
2. **etcd 備份 + PKI 備份 + KMS 金鑰備份**，三者缺一就無法還原；每季演練。
3. **憑證到期前 30 天告警**；更新後要重啟 static Pod，並自動化 kubelet CSR 核准。
4. **明確設定 systemReserved／kubeReserved 與驅逐門檻**，避免 Node 本身被壓垮。
5. **DR 以 GitOps + Velero + 資料層複寫**組合，依業務等級定義 RPO／RTO 並定期演練。

---

## 11. 升級策略

### 11.1 版本與支援政策

| 項目 | 規則 |
| --- | --- |
| 發布節奏 | 每年約 **3 個 minor 版本**（約每 15–17 週一版） |
| 支援期 | 每個 minor 約 **14 個月**：前 12 個月標準支援，之後 2 個月維護模式（只修重大安全與嚴重問題） |
| 同時支援 | 最新 3 個 minor 版本（實際上維護期重疊時會有 4 個） |
| Patch 版本 | 約每月一次（月中） |

**截至 2026-10-01 的支援狀態**（來源：kubernetes.io releases schedule）：

| 版本 | 發布日 | 進入維護模式 | EOL | 狀態 |
| --- | --- | --- | --- | --- |
| **1.37** | 2026-08-26 | 2027-08-28 | 2027-10-28 | 最新（v1.37.1，下一個 patch 1.37.2 預計 2026-10-13） |
| 1.36 | 2026-04-22 | 2027-04-28 | 2027-06-28 | 支援中（v1.36.5） |
| 1.35 | 2025-12-17 | 2026-12-28 | 2027-02-28 | 支援中（v1.35.9） |
| 1.34 | 2025-08-27 | 2026-08-27 | **2026-10-27** | **維護模式，即將 EOL**（v1.34.12） |
| 1.33 以前 | — | — | 已 EOL（1.33 於 2026-06-28） | 應立即升級 |

> ⚠️ **v2.0 更正**：v1.0 以 1.29 為基準，而 **1.29 已於 2025-02-28 EOL**。v1.0 的升級圖示（1.27 → 1.30）與範例版號都已過時。
>
> 📌 **雲端代管版本**：GKE、EKS、AKS 的支援期與上游不同（通常更長，並提供付費延長支援）。請以各雲端的版本行事曆為準。

---

### 11.2 Version Skew 政策（元件版本差距）

| 元件 | 允許的版本差距（相對 kube-apiserver） |
| --- | --- |
| kube-apiserver（HA 多台之間） | 最新與最舊相差**最多 1 個 minor** |
| kube-controller-manager、kube-scheduler、cloud-controller-manager | 不可比 apiserver 新；可以**舊 1 個 minor** |
| **kubelet** | 不可比 apiserver 新；可以**舊 3 個 minor**（1.25 起） |
| kube-proxy | 不可比 apiserver 新；可以舊 3 個 minor；和同 Node 的 kubelet 相差最多 3 個 minor |
| kubectl | apiserver **±1 個 minor** |

```mermaid
flowchart LR
    V34["1.34"] --> V35["1.35"] --> V36["1.36"] --> V37["1.37"]
    V34 -. "Control Plane 不可跳版" .-> V36
```

**重點**：

- **Control Plane 必須逐一 minor 升級**（1.34 → 1.35 → 1.36 → 1.37），不能跳版。
- **kubelet 可以落後**：Control Plane 連升三版時，Worker 可以停留在 1.34，最後再直接升到 1.37（kubelet 1.34 對 apiserver 1.37 仍在 skew 範圍內）。這能大幅減少 Node 的滾動次數。
- kubelet **不支援原地跨 minor 升級**：升級前必須先 drain Node。

> ⚠️ **v2.0 更正**：v1.0 寫「僅支援相鄰 Minor 版本升級」，沒有區分 Control Plane 與 kubelet。正確說法是 Control Plane 不可跳版，kubelet 可以落後最多 3 個 minor，因此 Worker 可以一次跨多版（但每個 Node 仍需 drain 後重新加入或升級）。

---

### 11.3 升級順序

```mermaid
flowchart TD
    A["0. 準備<br/>閱讀 Release Notes、檢查棄用 API、備份 etcd"] --> B["1. 第一台 Control Plane<br/>kubeadm upgrade apply"]
    B --> C["2. 其他 Control Plane<br/>kubeadm upgrade node"]
    C --> D["3. Control Plane 的 kubelet / kubectl"]
    D --> E["4. 叢集附加元件<br/>CNI、CoreDNS、CSI、Gateway、metrics-server"]
    E --> F["5. Worker Node（分批）<br/>cordon → drain → 升級 → uncordon"]
    F --> G["6. 驗證與觀察"]
```

> ⚠️ **v2.0 更正**：v1.0 的升級順序把「kubelet／kubectl」放在 Worker Node 之後，容易誤解為所有 Node 升級完才處理 kubelet。正確做法是每台 Node（含 Control Plane）在該 Node 升級時同時升級 kubelet。CNI 等附加元件請依其相容性表，在 Worker 升級前或同時更新。

---

### 11.4 棄用 API 與破壞性變更檢查

#### 11.4.1 檢查棄用 API

```bash
# 1. API Server 指標：哪些棄用 API 仍被呼叫（含移除版本）
kubectl get --raw /metrics | grep apiserver_requested_deprecated_apis

# 2. 掃描 Git 中的 manifest 與 Helm release（Pluto v5.24）
pluto detect-files -d ./manifests --target-versions k8s=v1.37.0
pluto detect-helm -o wide --target-versions k8s=v1.37.0

# 3. 從 Audit Log 找出呼叫者（annotation: k8s.io/deprecated="true"）
jq 'select(.annotations["k8s.io/deprecated"]=="true") | {user: .user.username, uri: .requestURI}' audit.log
```

> 📌 內建 API 自 **1.32**（移除 `flowcontrol.apiserver.k8s.io/v1beta3`）之後，到 1.37 都沒有再移除已 GA 資源的舊版 API。1.34→1.37 的風險主要來自**行為變更與元件需求**（見 11.4.2），以及 CRD／Operator 自身的 API 版本。

#### 11.4.2 1.34 → 1.37 逐版破壞性變更與注意事項

| 升級 | 必須處理的事項 |
| --- | --- |
| **1.34 → 1.35** | **cgroup v1 節點的 kubelet 預設無法啟動**（`failCgroupV1: true`）；kube-proxy `ipvs` 棄用（出現警告）；1.35 是最後支援 containerd 1.x 的版本；In-place resize GA；KYAML Beta |
| **1.35 → 1.36** | **必須 containerd 2.0 以上**；kubelet 不再從 `cgroupDriver` 設定後備，Runtime 必須支援 CRI `RuntimeConfig`；**`gitRepo` Volume 永久停用**；Service `externalIPs` 棄用（出現警告）；Ingress NGINX 已退役；User Namespaces、MAP、Image Volume GA |
| **1.36 → 1.37** | **static Pod 不可再引用 Secret／ConfigMap**（`PreventStaticPodAPIReferences` gate 已移除）；kube-dns 棄用；`kubectl run -f` 棄用；StatefulSet `maxUnavailable` 重新預設開啟；HPA scale-to-zero Beta 預設開啟；Pod 憑證、KYAML、metrics.k8s.io GA |

```bash
# 升級前快速檢查清單（在每個叢集執行）
# 1. cgroup 版本（每台 Node）
stat -fc %T /sys/fs/cgroup/                 # 必須是 cgroup2fs
# 2. Container Runtime 版本
kubectl get nodes -o custom-columns=NAME:.metadata.name,RUNTIME:.status.nodeInfo.containerRuntimeVersion
# 3. kubelet 是否回報即將失去支援的 Runtime
kubectl get --raw "/api/v1/nodes/<node>/proxy/metrics" | grep kubelet_cri_losing_support
# 4. 是否仍使用 gitRepo volume
kubectl get pods -A -o json | jq -r '.items[] | select(any(.spec.volumes[]?; has("gitRepo"))) | "\(.metadata.namespace)/\(.metadata.name)"'
# 5. 是否仍使用 externalIPs
kubectl get svc -A -o json | jq -r '.items[] | select(.spec.externalIPs != null) | "\(.metadata.namespace)/\(.metadata.name)"'
# 6. kube-proxy 模式
kubectl -n kube-system get cm kube-proxy -o jsonpath='{.data.config\.conf}' | grep 'mode:'
```

---

### 11.5 kubeadm 升級流程

以下以 **1.36.5 → 1.37.1** 為例。

#### 11.5.1 第一台 Control Plane

```bash
# 0. 切換 pkgs.k8s.io repo 到新的 minor 版本（每個 minor 是獨立 repo）
sudo sed -i 's#/v1.36/#/v1.37/#g' /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
apt-cache madison kubeadm | head -3

# 1. 升級 kubeadm
sudo apt-mark unhold kubeadm
sudo apt-get install -y kubeadm='1.37.1-*'
sudo apt-mark hold kubeadm
kubeadm version

# 2. 檢查升級計畫（顯示各元件目標版本與需要手動升級的設定）
sudo kubeadm upgrade plan

# 3. 執行升級（會自動更新 Control Plane 憑證）
sudo kubeadm upgrade apply v1.37.1

# 4. drain 本機 Node，升級 kubelet 與 kubectl
kubectl drain cp1 --ignore-daemonsets
sudo apt-mark unhold kubelet kubectl
sudo apt-get install -y kubelet='1.37.1-*' kubectl='1.37.1-*'
sudo apt-mark hold kubelet kubectl
sudo systemctl daemon-reload
sudo systemctl restart kubelet
kubectl uncordon cp1
```

#### 11.5.2 其他 Control Plane

```bash
# repo 切換與 kubeadm 升級同上，然後：
sudo kubeadm upgrade node
# 再 drain → 升級 kubelet/kubectl → restart kubelet → uncordon
```

#### 11.5.3 Worker Node（分批進行）

```bash
# 在管理端
kubectl cordon worker-12
kubectl drain worker-12 --ignore-daemonsets --delete-emptydir-data --timeout=15m

# 在 worker-12 上
sudo sed -i 's#/v1.36/#/v1.37/#g' /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-mark unhold kubeadm kubelet kubectl
sudo apt-get install -y kubeadm='1.37.1-*'
sudo kubeadm upgrade node
sudo apt-get install -y kubelet='1.37.1-*' kubectl='1.37.1-*'
sudo apt-mark hold kubeadm kubelet kubectl
sudo systemctl daemon-reload
sudo systemctl restart kubelet

# 回到管理端
kubectl uncordon worker-12
kubectl get node worker-12
```

> ⚠️ **v2.0 更正**：v1.0 的升級範例沒有切換 pkgs.k8s.io 的 repo 路徑，照做會找不到新版套件；Worker Node 升級時也漏了 `apt-mark unhold`。另外，**不可變基礎架構（Immutable Infrastructure）**是更好的做法：用新版映像建立新 Node、加入叢集、drain 舊 Node 後刪除（Cluster API、Karpenter、雲端 Node Pool 升級都是這個模式）。

---

### 11.6 Managed Kubernetes 升級

| 項目 | 做法 |
| --- | --- |
| Control Plane | 由雲端執行（通常一鍵或依 Release Channel 自動升級），仍需逐版 |
| Node Pool | 建立新版 Node Pool 後遷移（藍綠），或使用 surge 升級設定 |
| 維護窗口 | 設定維護時段與排除期間（例如月底結帳、年節） |
| 升級前檢查 | 雲端主控台的升級洞察（例如 EKS Upgrade Insights、GKE 棄用洞察）會列出棄用 API 用量 |
| 延長支援 | 落後版本會進入付費延長支援，應視為「技術債利息」 |

---

### 11.7 應用程式升級注意事項

PodDisruptionBudget 是升級期間保護應用的關鍵，設定方式見 [6.3.4](#634-pod-disruption-budgetpdb)。升級前請確認：

```bash
# 找出會讓 drain 卡住的 PDB（ALLOWED DISRUPTIONS = 0）
kubectl get pdb -A
kubectl get pdb -A -o json | jq -r '.items[] | select(.status.disruptionsAllowed==0) | "\(.metadata.namespace)/\(.metadata.name)"'
```

| 檢查項 | 說明 |
| --- | --- |
| PDB 是否允許至少 1 個中斷 | 單副本 + `minAvailable: 1` 會卡住 drain |
| 應用能否承受 Pod 重新排程 | Graceful shutdown、readiness、連線重試 |
| Operator／CRD 相容性 | Operator 是否支援新版 Kubernetes（查看相容性表） |
| Helm chart 的 `kubeVersion` 限制 | 舊 chart 可能限制最高版本 |
| Webhook 可用性 | Webhook Pod 被驅逐時不應阻擋其他 Pod 重新建立（`failurePolicy`、排除 kube-system） |

---

### 11.8 升級前檢查清單

**事前準備**

- [ ] 閱讀目標版本與中間每一版的 Release Notes、Urgent Upgrade Notes
- [ ] 確認目前版本與目標版本的路徑（Control Plane 逐版）
- [ ] 執行 [11.4.2](#1142-134--137-逐版破壞性變更與注意事項) 的快速檢查（cgroup v2、containerd 2.x、gitRepo、externalIPs、kube-proxy 模式）
- [ ] 以 Pluto 與 `apiserver_requested_deprecated_apis` 檢查棄用 API
- [ ] 確認 CNI、CSI、Gateway 實作、Operator、監控元件支援目標版本
- [ ] 備份 etcd、`/etc/kubernetes/pki`、kubeadm 設定
- [ ] 確認所有關鍵服務的 PDB 允許中斷
- [ ] 在測試叢集完整演練一次
- [ ] 安排維護窗口並通知相關團隊

**升級執行**

- [ ] 升級第一台 Control Plane 並驗證 `/readyz`
- [ ] 升級其餘 Control Plane
- [ ] 升級附加元件（CNI、CoreDNS、CSI）
- [ ] 分批升級 Worker Node，每批完成後觀察指標

**升級後驗證**

- [ ] `kubectl get nodes` 版本正確且全部 Ready
- [ ] `kube-system` 與平台 Namespace 的 Pod 全部正常
- [ ] 應用 SLO（錯誤率、延遲）正常
- [ ] 監控、日誌、告警正常
- [ ] 執行冒煙測試與 E2E 測試
- [ ] 更新版本盤點紀錄

---

### 11.9 💡 本章實務建議

1. **每年至少升級 2–3 個 minor 版本**，永遠不要停留在 EOL 版本；1.34 叢集請在 2026-10-27 前升級。
2. **Control Plane 逐版、kubelet 可以一次跨多版**，善用 skew 政策減少 Node 滾動次數。
3. **升級的主要風險是行為變更**：1.35 的 cgroup v2、1.36 的 containerd 2.x 是最常見的卡關點，要提前完成 OS 與 Runtime 升級。
4. **優先採用不可變 Node**：用新映像建立新 Node 取代原地升級。
5. **升級演練與檢查清單自動化**，納入平台團隊的季度計畫。

---

## 12. CI/CD 與 GitOps

### 12.1 CI/CD 整體流程

```mermaid
flowchart LR
    Dev["開發者"] --> AppRepo["應用 Repo<br/>原始碼 + Dockerfile"]
    AppRepo --> CI["CI Pipeline<br/>測試 → 建置 → 掃描 → SBOM → 簽章"]
    CI --> Reg["企業 Registry<br/>Harbor / ECR / ACR"]
    CI -- "更新映像 tag / digest" --> CfgRepo["設定 Repo<br/>Helm values / Kustomize"]
    CfgRepo --> GitOps["Argo CD / Flux<br/>Pull 模式同步"]
    GitOps --> K8s["Kubernetes 叢集<br/>dev → staging → prod"]
    Reg --> K8s
```

| 模式 | 做法 | 優點 | 缺點 |
| --- | --- | --- | --- |
| **Push**（CI 直接 kubectl／helm） | CI 持有叢集憑證並套用 | 簡單 | CI 需要高權限叢集憑證；叢集狀態可能偏離 Git |
| **Pull（GitOps）** | 叢集內的 Argo CD／Flux 從 Git 拉取並調和 | 不需要對外暴露叢集憑證；自動修正漂移；Git 即稽核紀錄 | 需要維運 GitOps 工具 |

> 📌 **企業建議**：正式環境採用 **GitOps（Pull 模式）**，CI 只負責產出映像並更新設定 Repo。v1.0 的 GitLab CI 範例屬於 Push 模式，本版保留作為開發／測試環境參考，並修正其問題。

---

### 12.2 GitLab CI 範例

```yaml
# .gitlab-ci.yml
stages: [test, build, scan, deploy]

variables:
  IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
  KUBECTL_VERSION: "v1.37.1"

test:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn -B verify

build:
  stage: build
  image: docker:29.8.2                     # 固定版本，不使用 docker:latest
  services:
    - name: docker:29.8.2-dind
      alias: docker
  variables:
    DOCKER_TLS_CERTDIR: "/certs"
  script:
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
    - docker build --pull -t "$IMAGE" .
    - docker push "$IMAGE"
    # 取得 digest，後續部署以 digest 為準
    - docker inspect --format='{{index .RepoDigests 0}}' "$IMAGE" | tee image-digest.txt
  artifacts:
    paths: [image-digest.txt]

scan:
  stage: scan
  image:
    name: aquasec/trivy:0.74.0
    entrypoint: [""]
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL --ignore-unfixed "$(cat image-digest.txt)"
    - trivy image --format cyclonedx --output sbom.cdx.json "$(cat image-digest.txt)"
  artifacts:
    paths: [sbom.cdx.json]

# 開發環境：Push 模式直接部署
deploy-dev:
  stage: deploy
  image: alpine:3.24
  environment:
    name: dev
  before_script:
    # 從官方 dl.k8s.io 下載固定版本 kubectl 並驗證 checksum
    - apk add --no-cache curl
    - curl -fsSLO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
    - curl -fsSLO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl.sha256"
    - echo "$(cat kubectl.sha256)  kubectl" | sha256sum -c -
    - install -m 0755 kubectl /usr/local/bin/kubectl
  script:
    - kubectl config use-context ecommerce/agent:dev     # GitLab Agent for Kubernetes 提供的 context
    - kubectl set image deployment/order-service order-service="$(cat image-digest.txt)" -n order-dev
    - kubectl rollout status deployment/order-service -n order-dev --timeout=10m

# 正式環境：只更新設定 Repo，由 Argo CD 同步
promote-prod:
  stage: deploy
  image: alpine:3.24
  when: manual
  environment:
    name: production
  before_script:
    - apk add --no-cache git
  script:
    - git clone "https://oauth2:${CONFIG_REPO_TOKEN}@gitlab.example.com/platform/ecommerce-config.git"
    - cd ecommerce-config/apps/order-service/overlays/prod
    - 'sed -i "s|newTag: .*|newTag: \"$CI_COMMIT_SHORT_SHA\"|" kustomization.yaml'
    - git commit -am "order-service: promote $CI_COMMIT_SHORT_SHA to prod"
    - git push
```

> ⚠️ **v2.0 更正**：
>
> - v1.0 使用 `docker:latest` 與 `bitnami/kubectl:latest`。**Bitnami 已於 2025 年 8–9 月下架免費的版本化映像**（舊映像移到 `bitnamilegacy`，不再更新），`bitnami/kubectl` 已無法從原位置取得。本版改為從官方 `dl.k8s.io` 下載固定版本並驗證 checksum。
> - v1.0 以 `kubectl config use-context` 搭配 CI 內的長效憑證。建議改用 **GitLab Agent for Kubernetes**（叢集主動連出，不必在 CI 保存 kubeconfig）或 OIDC 短效 Token。
> - 部署改以 **digest** 指定映像，避免 tag 被覆蓋。
> - Kaniko 已於 2025 年封存（Google 停止維護），需要無 Docker daemon 的建置時，可改用 BuildKit rootless（v0.33）或 Buildah（v1.45）。

---

### 12.3 容器映像管理策略

#### 12.3.1 映像命名規範

```text
<registry>/<project>/<image>:<tag>@<digest>

範例：
registry.example.com/ecommerce/order-service:1.4.2
registry.example.com/ecommerce/order-service:1.4.2-a1b2c3d
registry.example.com/ecommerce/order-service@sha256:4f53c8...（部署時最精確）
```

#### 12.3.2 映像標籤策略

| 標籤類型 | 範例 | 用途 | 正式環境 |
| --- | --- | --- | --- |
| 語意版本 | `1.4.2` | 正式發佈 | ✅ |
| 版本 + Git SHA | `1.4.2-a1b2c3d` | 可追溯 | ✅ |
| Git SHA | `a1b2c3d` | 每次 commit | 可用於 dev／staging |
| **Digest** | `@sha256:...` | 不可變 | ✅ **最建議** |
| `latest` | `latest` | — | ❌ **禁止**（以 VAP 強制，見 8.5.1） |

#### 12.3.3 Registry 治理

| 項目 | 建議 |
| --- | --- |
| 企業 Registry | Harbor（CNCF 畢業）、雲端 ECR／ACR／Artifact Registry |
| 外部映像 | 透過 Registry proxy cache 或鏡像同步，不讓 Node 直接連 Docker Hub（也避免 rate limit） |
| Tag 不可變 | 在 Registry 設定 tag immutability |
| 保留政策 | 自動清理未使用的舊映像，但保留正式版本與其 SBOM／簽章 |
| 掃描 | 推送時掃描 + 每日重掃（新 CVE 會持續出現） |

---

### 12.4 Helm 4

Helm **v4.0 於 2025-11 發布**，目前最新 **v4.3.0**。Helm 3 已於 2026-09-09 停止 bug 修正，**安全修正到 2027-02-10 為止**，請規劃遷移。

#### 12.4.1 Helm 4 相對 Helm 3 的主要變化

| 項目 | Helm 3 | Helm 4 |
| --- | --- | --- |
| 套用方式 | Client-side 三方合併 | **新 release 預設 Server-Side Apply**；從 Helm 3 升級的既有 release 沿用 client-side |
| Plugin | 執行檔 | 新增 **WebAssembly（Wasm）plugin** 執行環境（沙箱化）；post-renderer 改為 plugin |
| 旗標 | `--atomic`、`--force` | 改名為 `--rollback-on-failure`、`--force-replace`（舊旗標仍可用但有警告） |
| Registry 登入 | 可接受 URL | `helm registry login` 只接受網域名稱 |
| Chart API | v2 | Chart v2 持續支援（Chart v3 規劃中） |

#### 12.4.2 Chart 結構

```text
order-service/
├── Chart.yaml              # Chart 中繼資料（apiVersion: v2）
├── values.yaml             # 預設值
├── values.schema.json      # values 的 JSON Schema 驗證（強烈建議）
├── templates/
│   ├── _helpers.tpl        # 共用模板（名稱、標籤）
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── httproute.yaml      # Gateway API 路由
│   ├── hpa.yaml
│   ├── pdb.yaml
│   ├── networkpolicy.yaml
│   └── servicemonitor.yaml
└── charts/                 # 相依的 chart
```

#### 12.4.3 Helm 常用指令

```bash
# 安裝或升級（同一個指令）
helm upgrade --install order-service ./order-service \
  -n order-prod -f values-prod.yaml \
  --rollback-on-failure --wait --timeout 10m

# 查看渲染結果、差異（helm-diff plugin）
helm template order-service ./order-service -f values-prod.yaml
helm diff upgrade order-service ./order-service -n order-prod -f values-prod.yaml

# 歷史與回滾
helm history order-service -n order-prod
helm rollback order-service 7 -n order-prod

# OCI Registry 發佈 chart
helm package ./order-service
helm push order-service-1.4.2.tgz oci://registry.example.com/charts
helm install order-service oci://registry.example.com/charts/order-service --version 1.4.2
```

#### 12.4.4 values.yaml 範例

```yaml
replicaCount: 3

image:
  repository: registry.example.com/ecommerce/order-service
  tag: "1.4.2"
  digest: ""                 # 有值時優先使用 digest
  pullPolicy: IfNotPresent

resources:
  requests:
    cpu: 500m
    memory: 1Gi
  limits:
    memory: 1Gi

service:
  port: 80
  targetPort: 8080

route:                       # Gateway API HTTPRoute
  enabled: true
  parentRefs:
    - name: public-gw
      namespace: edge
      sectionName: https
  hostnames: [api.example.com]
  pathPrefix: /orders

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 30
  targetCPUUtilizationPercentage: 70

pdb:
  maxUnavailable: 1

env:
  SPRING_PROFILES_ACTIVE: production
```

> ⚠️ **v2.0 更正**：v1.0 的 values 以 `ingress` 區塊為主；本版改為 Gateway API `route`，並加上 PDB、HPA 開關與 digest 支援。

---

### 12.5 Kustomize

Kustomize（v5.8）以「base + overlay」方式管理多環境，已內建於 kubectl（`kubectl apply -k`）。

```text
apps/order-service/
├── base/
│   ├── kustomization.yaml
│   ├── deployment.yaml
│   └── service.yaml
└── overlays/
    ├── staging/
    │   └── kustomization.yaml
    └── prod/
        ├── kustomization.yaml
        └── patch-replicas.yaml
```

```yaml
# overlays/prod/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: order-prod
resources:
  - ../../base
labels:
  - pairs:
      example.com/env: prod
images:
  - name: registry.example.com/ecommerce/order-service
    newTag: "1.4.2"
configMapGenerator:
  - name: order-service-config
    files:
      - application.yaml
patches:
  - path: patch-replicas.yaml
```

| 選擇 | Helm | Kustomize |
| --- | --- | --- |
| 適合 | 可重用、可發佈的套件；第三方軟體 | 自家應用的多環境差異 |
| 學習曲線 | 模板語法較複雜 | 純 YAML |
| 常見組合 | 第三方元件用 Helm；自家應用用 Kustomize 或「Helm + Kustomize overlay」 | — |

---

### 12.6 GitOps：Argo CD 與 Flux

| 面向 | Argo CD（v3.5） | Flux（v2.9） |
| --- | --- | --- |
| 架構 | 集中式，有 Web UI 與 SSO | 分散式控制器，CLI／CRD 為主 |
| 多叢集 | 一個 Argo CD 管多叢集；ApplicationSet 大量產生 | 每個叢集各自執行 Flux |
| 映像自動更新 | Argo CD Image Updater | 內建 image-reflector／automation |
| 適合 | 需要 UI、多團隊自助、集中治理 | 偏好輕量、Git 為唯一介面 |

```yaml
# Argo CD Application（正式環境：自動同步 + 自我修復，但刪除需人工）
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: order-service-prod
  namespace: argocd
spec:
  project: ecommerce
  source:
    repoURL: https://gitlab.example.com/platform/ecommerce-config.git
    targetRevision: main
    path: apps/order-service/overlays/prod
  destination:
    server: https://kubernetes.default.svc
    namespace: order-prod
  syncPolicy:
    automated:
      prune: false             # 正式環境避免誤刪；改由人工確認
      selfHeal: true           # 手動修改會被還原成 Git 狀態
    syncOptions:
      - ServerSideApply=true
      - CreateNamespace=false  # Namespace 由平台範本建立
    retry:
      limit: 3
      backoff:
        duration: 30s
        factor: 2
```

> 📌 **Argo CD 3.x 重點**：3.0 起預設行為更安全（例如細粒度 RBAC 不再隱含繼承、資源追蹤預設改用 annotation），從 2.x 升級前請閱讀官方升級說明。AppProject 要限制可部署的 Namespace、叢集與資源類型，避免應用團隊透過 GitOps 繞過 RBAC。

### 12.7 環境晉升（Promotion）

```mermaid
flowchart LR
    C["commit a1b2c3d"] --> D["dev<br/>自動部署"]
    D -->|自動測試通過| S["staging<br/>自動更新 tag"]
    S -->|變更單核准<br/>（Merge Request）| P["prod<br/>Argo CD 同步"]
```

| 原則 | 說明 |
| --- | --- |
| 同一個映像 digest 一路晉升 | 不在各環境重新建置 |
| 晉升 = 修改設定 Repo 的 MR | 審核、簽核、稽核都在 Git 完成 |
| 正式環境變更需雙人審核 | 以 Git 平台的 Protected Branch + Code Owners 實作 |
| 環境差異只放在 overlay／values | base 保持一致 |

---

### 12.8 💡 本章實務建議

1. **正式環境一律 GitOps**；CI 不持有正式叢集的寫入憑證。
2. **映像以 digest 部署、全面禁止 `latest`**，CI 工具映像也要固定版本（避免再發生 Bitnami 下架這類事件）。
3. **CI 管線包含測試、掃描、SBOM、簽章**，未通過不得晉升。
4. **Helm 3 使用者在 2027-02 前遷移到 Helm 4**，並留意 Server-Side Apply 帶來的欄位擁有權變化。
5. **AppProject／Flux Tenant 要限制權限範圍**，GitOps 工具本身是高權限元件，需納入資安控管。

---

## 13. 應用系統整合

### 13.1 外部資料庫與既有系統

在企業環境中，資料庫、MQ、主機系統常在 Kubernetes 外部。建議在叢集內為它們建立 Service，讓應用以固定的叢集內名稱存取，外部位址變更時只需要改一處。

#### 13.1.1 方式一：ExternalName（外部有 DNS 名稱）

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders-db
  namespace: order-prod
spec:
  type: ExternalName
  externalName: orders-db.prod.db.example.internal   # 回傳 CNAME
```

> ⚠️ ExternalName 只做 DNS CNAME，**不做埠對應**；使用 TLS 時，憑證的 SAN 必須包含外部名稱（應用連線時要用外部名稱驗證憑證，或在憑證加入叢集內名稱）。

#### 13.1.2 方式二：無 selector 的 Service + EndpointSlice（外部只有 IP）

```yaml
apiVersion: v1
kind: Service
metadata:
  name: legacy-db
  namespace: order-prod
spec:
  ports:
    - name: postgres
      port: 5432
      targetPort: 5432
---
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: legacy-db-1
  namespace: order-prod
  labels:
    kubernetes.io/service-name: legacy-db           # 必須：對應到 Service
    endpointslice.kubernetes.io/managed-by: platform-team   # 標示為人工管理，避免被控制器覆蓋
addressType: IPv4
ports:
  - name: postgres                                  # 必須與 Service 的埠名稱相同
    port: 5432
    protocol: TCP
endpoints:
  - addresses: ["10.20.30.100"]
    conditions:
      ready: true
  - addresses: ["10.20.30.101"]
    conditions:
      ready: true
```

> ⚠️ **v2.0 更正**：v1.0 使用 `kind: Endpoints`，該 API 自 1.33 起棄用。改用 EndpointSlice 時，`kubernetes.io/service-name` 標籤與埠名稱必須正確，否則 Service 不會有後端。

#### 13.1.3 連線治理

| 項目 | 建議 |
| --- | --- |
| 連線池 | Pod 數 × 每 Pod 連線池上限 ≤ 資料庫最大連線數；HPA 擴容時特別注意（可用 PgBouncer 等中介） |
| Egress 控管 | NetworkPolicy 只允許特定 Pod 連到資料庫網段 |
| 防火牆 | 外部防火牆以 Node 網段或 Egress Gateway 的固定 IP 放行（Pod IP 會變） |
| 憑證與密碼 | 由 External Secrets 從 Vault 取得，支援輪替（13.3） |

---

### 13.2 Prometheus 整合

應用指標的收集方式見 [9.2.3 以 ServiceMonitor 收集應用指標](#923-以-servicemonitor-收集應用指標)。整合要點：

- 應用提供 `/actuator/prometheus`（Spring Boot Micrometer）或 OTLP 匯出。
- ServiceMonitor 放在**應用自己的 Namespace**，由應用團隊和 Deployment 一起維護。
- 告警規則（`PrometheusRule`）也隨應用版本控制，例如錯誤率與延遲的 SLO 告警。

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: order-service-slo
  namespace: order-prod
spec:
  groups:
    - name: order-service.slo
      rules:
        - alert: OrderServiceHighErrorRate
          expr: |
            sum(rate(http_server_requests_seconds_count{namespace="order-prod",service="order-service",status=~"5.."}[5m]))
            /
            sum(rate(http_server_requests_seconds_count{namespace="order-prod",service="order-service"}[5m])) > 0.01
          for: 10m
          labels:
            severity: critical
            team: order
          annotations:
            summary: "order-service 5xx 錯誤率超過 1%"
            runbook_url: "https://wiki.example.com/runbooks/order-service#high-error-rate"
```

---

### 13.3 External Secrets Operator 與 Vault

External Secrets Operator（ESO，v2.11.0，API `external-secrets.io/v1`）把外部 Secret 管理系統（HashiCorp Vault、AWS Secrets Manager、Azure Key Vault、GCP Secret Manager 等）的資料同步成 Kubernetes Secret，Git 中只保存「參照」。

```mermaid
flowchart LR
    V["Vault / 雲端 Secret Manager"] -- "讀取（短效 Token）" --> ESO["External Secrets Operator"]
    ESO -- "建立／更新" --> S["Kubernetes Secret"]
    S --> P["應用 Pod"]
    G["Git：ExternalSecret（只有參照）"] --> ESO
```

```yaml
# 1. 平台團隊：ClusterSecretStore（以 Kubernetes ServiceAccount 向 Vault 認證）
apiVersion: external-secrets.io/v1
kind: ClusterSecretStore
metadata:
  name: vault-prod
spec:
  provider:
    vault:
      server: https://vault.example.internal:8200
      path: kv
      version: v2
      auth:
        kubernetes:
          mountPath: kubernetes-prod
          role: external-secrets
          serviceAccountRef:
            name: external-secrets
            namespace: external-secrets
---
# 2. 應用團隊：ExternalSecret
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: order-db-credentials
  namespace: order-prod
spec:
  refreshInterval: 1h
  secretStoreRef:
    kind: ClusterSecretStore
    name: vault-prod
  target:
    name: order-db-credentials       # 產生的 Kubernetes Secret 名稱
    creationPolicy: Owner
  data:
    - secretKey: username
      remoteRef:
        key: ecommerce/order-service/db
        property: username
    - secretKey: password
      remoteRef:
        key: ecommerce/order-service/db
        property: password
```

| 方案 | 說明 | 適用 |
| --- | --- | --- |
| **External Secrets Operator** | 同步外部系統到 K8s Secret | **企業首選**，已有 Vault／雲端 Secret Manager |
| Secrets Store CSI Driver | 以 Volume 掛載，可選擇不建立 K8s Secret | 不希望 Secret 存在 etcd |
| Sealed Secrets | 以叢集公鑰加密後放進 Git | 小型團隊、沒有外部 Secret 系統 |
| SOPS（+ Flux／Argo CD 外掛） | 以 KMS／age 加密 YAML 欄位 | GitOps 原生加密 |
| Vault Agent Injector | Sidecar 直接寫入檔案 | 已深度使用 Vault |

> 📌 **注意**：ESO 只支援最新的 minor 版本，官方相容性表中 v2.11 標示的測試版本為 Kubernetes 1.36。在 1.37 叢集上使用前，請先在測試環境驗證，並追蹤 ESO 的下一個版本。Secret 輪替後，以環境變數使用的 Pod 不會自動更新，需要搭配 Reloader 或 `rollout restart`。

---

### 13.4 cert-manager 憑證自動化

cert-manager（v1.21）負責簽發與自動續期 TLS 憑證，支援企業 CA、Vault PKI、ACME（Let's Encrypt）等。

```yaml
# 企業內部 CA（以 Vault PKI 為例）
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: corp-ca-issuer
spec:
  vault:
    server: https://vault.example.internal:8200
    path: pki_int/sign/k8s-gateway
    auth:
      kubernetes:
        mountPath: /v1/auth/kubernetes-prod
        role: cert-manager
        serviceAccountRef:
          name: cert-manager-vault
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: wildcard-example-com
  namespace: edge
spec:
  secretName: wildcard-example-com-tls     # 對應 Gateway listener 的 certificateRefs
  duration: 2160h                          # 90 天
  renewBefore: 360h                        # 到期前 15 天續期
  privateKey:
    algorithm: ECDSA
    size: 256
    rotationPolicy: Always
  dnsNames:
    - "*.example.com"
  issuerRef:
    kind: ClusterIssuer
    name: corp-ca-issuer
```

> 📌 cert-manager 也支援直接監看 **Gateway API 的 Gateway 資源**：在 Gateway 加上 `cert-manager.io/cluster-issuer` 註解，即可依 listener 的 hostname 自動建立 Certificate（需在 cert-manager 啟用 Gateway API 支援）。

---

### 13.5 Spring Boot 優雅關機與零停機發版

#### 13.5.1 Kubernetes 端設定

```yaml
spec:
  terminationGracePeriodSeconds: 60      # 必須大於 preStop + 應用關機時間
  containers:
    - name: app
      lifecycle:
        preStop:
          sleep:
            seconds: 10                  # 1.34 GA：等待負載平衡器移除本 Pod
      readinessProbe:
        httpGet:
          path: /actuator/health/readiness
          port: 8080
```

#### 13.5.2 Spring Boot 端設定

```yaml
# application.yaml
server:
  shutdown: graceful                     # Spring Boot 3.4 起預設即為 graceful
spring:
  lifecycle:
    timeout-per-shutdown-phase: 30s      # 等待進行中請求完成的上限
management:
  endpoint:
    health:
      probes:
        enabled: true                    # 提供 /actuator/health/liveness 與 /readiness
  endpoints:
    web:
      exposure:
        include: health,prometheus
```

**時間軸**：

```mermaid
sequenceDiagram
    participant K as kubelet
    participant LB as Gateway / kube-proxy
    participant A as Spring Boot
    K->>A: 開始終止（Pod Terminating）
    K->>LB: EndpointSlice 標記 not ready（平行）
    K->>A: preStop sleep 10 秒（仍可處理請求）
    LB->>LB: 規則更新完成，不再送新請求
    K->>A: SIGTERM
    A->>A: graceful shutdown：拒絕新請求，等待進行中請求（最多 30 秒）
    A->>K: 程序結束
```

> ⚠️ **v2.0 更正**：v1.0 用 `@PreDestroy` 示範優雅關機，但 `@PreDestroy` 只是 Bean 銷毀回呼，不會等待進行中的 HTTP 請求。正確做法是 `server.shutdown=graceful` + `timeout-per-shutdown-phase`。v1.0 的 `preStop` 使用 `sh -c "sleep 10"`，在 distroless 映像中會因為沒有 shell 而失敗；1.34 起請改用原生 `sleep` 動作。

**計算原則**：`terminationGracePeriodSeconds` ≥ `preStop` 秒數 + `timeout-per-shutdown-phase` + 緩衝（5–10 秒）。

---

### 13.6 💡 本章實務建議

1. **外部系統一律透過叢集內 Service 存取**，外部只有 IP 時使用 EndpointSlice，不再使用 Endpoints。
2. **Secret 以 ESO + Vault／雲端 Secret Manager 管理**，搭配 Reloader 處理輪替。
3. **憑證全面交給 cert-manager**，到期告警作為最後一道防線。
4. **零停機發版三件事**：Readiness Probe、`preStop.sleep`、應用 graceful shutdown，缺一不可。
5. **監控規則與應用一起版本控制**（ServiceMonitor、PrometheusRule 放在應用 Repo 或設定 Repo）。

---

## 14. 最佳實踐與常見反模式

### 14.1 建議遵循的設計原則

#### 14.1.1 最佳實踐清單

| 類別 | 實踐 | 說明 | 章節 |
| --- | --- | --- | --- |
| **資源管理** | 設定 request 與 memory limit | 排程與驅逐行為可預測 | 6.1 |
| **資源管理** | LimitRange + ResourceQuota | Namespace 層級的護欄 | 10.1 |
| **高可用** | ≥ 3 副本 + 跨區拓撲分散 | 單一 Node／可用區故障不中斷 | 3.3、6.3 |
| **高可用** | PDB（`maxUnavailable: 1`） | 升級、縮容時不中斷 | 6.3.4 |
| **健康檢查** | Startup／Liveness／Readiness 分工 | 自動恢復、零停機 | 6.2 |
| **發版** | `maxUnavailable: 0` + `preStop` + graceful shutdown | 零停機 | 7.5、13.5 |
| **安全性** | PSA `restricted` + non-root + drop ALL | 降低攻擊面 | 8.4 |
| **安全性** | default-deny NetworkPolicy | 零信任網路 | 4.9 |
| **安全性** | OIDC + 最小權限 RBAC | 可稽核、可撤銷 | 8.1、8.2 |
| **安全性** | KMS v2 + External Secrets | Secret 不落地、不進 Git | 8.6、13.3 |
| **供應鏈** | 掃描 + SBOM + 簽章 + digest 部署 | 可追溯、防竄改 | 8.10、12.3 |
| **流量** | Gateway API | 標準化、可攜、多租戶 | 4.7 |
| **可觀測性** | 結構化日誌 + 指標 + 追蹤 + 事件 | 快速定位問題 | 9 |
| **版本控制** | GitOps 管理所有 YAML | 可追溯、可審計、可重建 | 12.6 |
| **生命週期** | 每年升級 2–3 個 minor | 避免 EOL 與延長支援費 | 11 |

#### 14.1.2 企業標準工作負載範本（整合範例）

以下範本整合本手冊的建議，可作為企業內部 Helm chart／Kustomize base 的起點：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-api
  namespace: payment-prod
  labels:
    app.kubernetes.io/name: payment-api
    app.kubernetes.io/part-of: payment
    app.kubernetes.io/version: "5.0.0"
    example.com/team: payment
spec:
  replicas: 3
  revisionHistoryLimit: 10
  progressDeadlineSeconds: 600
  minReadySeconds: 10
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app.kubernetes.io/name: payment-api
  template:
    metadata:
      labels:
        app.kubernetes.io/name: payment-api
        app.kubernetes.io/version: "5.0.0"
        example.com/team: payment
    spec:
      serviceAccountName: payment-api
      automountServiceAccountToken: false
      priorityClassName: business-critical
      terminationGracePeriodSeconds: 60
      securityContext:
        runAsNonRoot: true
        runAsUser: 10001
        fsGroup: 10001
        seccompProfile:
          type: RuntimeDefault
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              app.kubernetes.io/name: payment-api
        - maxSkew: 1
          topologyKey: kubernetes.io/hostname
          whenUnsatisfiable: ScheduleAnyway
          labelSelector:
            matchLabels:
              app.kubernetes.io/name: payment-api
      containers:
        - name: payment-api
          # 以 digest 部署（範例值，實際由 CI 產生）
          image: registry.example.com/payment/api@sha256:9b2f0c7e1d4a5b6c8e3f2a1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b
          ports:
            - name: http
              containerPort: 8080
          env:
            - name: JAVA_TOOL_OPTIONS
              value: "-XX:MaxRAMPercentage=75.0 -XX:+ExitOnOutOfMemoryError"
          envFrom:
            - secretRef:
                name: payment-api-secrets
          resources:
            requests:
              cpu: "1"
              memory: 2Gi
            limits:
              memory: 2Gi
          startupProbe:
            httpGet: {path: /actuator/health/liveness, port: http}
            periodSeconds: 5
            failureThreshold: 36
          livenessProbe:
            httpGet: {path: /actuator/health/liveness, port: http}
            periodSeconds: 10
            timeoutSeconds: 3
          readinessProbe:
            httpGet: {path: /actuator/health/readiness, port: http}
            periodSeconds: 5
            timeoutSeconds: 3
          lifecycle:
            preStop:
              sleep:
                seconds: 10
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          volumeMounts:
            - name: tmp
              mountPath: /tmp
      volumes:
        - name: tmp
          emptyDir:
            sizeLimit: 256Mi
```

> 📌 搭配的資源：Service（具名埠、`appProtocol`）、HTTPRoute、HPA、PDB、NetworkPolicy、ServiceMonitor、PrometheusRule、ExternalSecret。這些物件應該在同一個 chart／overlay 中一起交付。

---

### 14.2 常見錯誤與踩雷經驗

#### 14.2.1 常見反模式

| 反模式 | 問題 | 建議做法 |
| --- | --- | --- |
| 使用 `latest` 標籤 | 版本不可控、無法回滾 | 語意版本 + digest，以 VAP 禁止 |
| 沒有設定資源 request／limit | 排程不準、吵鬧鄰居、OOM 時被優先驅逐 | 必須設定；LimitRange 補預設值 |
| Memory limit 遠大於 request | Node 壓力時被驅逐、JVM heap 超出預期 | Memory limit = request |
| 所有服務都設 CPU limit | CFS 節流造成延遲尖峰 | 依服務性質決定（6.1.3） |
| Liveness 檢查外部依賴 | 依賴故障造成連鎖重啟 | Liveness 只檢查自身 |
| 單一副本部署關鍵服務 | 沒有高可用，升級必中斷 | 至少 3 副本 + PDB |
| 單副本 + `minAvailable: 1` | Node 永遠無法 drain | 改用 `maxUnavailable` 或提高副本數 |
| Secret 放進 Git（即使是 Base64） | 等同公開密碼 | External Secrets／Sealed Secrets／SOPS |
| 應用 Pod 自動掛載 SA Token | Pod 被入侵後可以呼叫 K8s API | `automountServiceAccountToken: false` |
| 使用 `hostPath`、`privileged` | 容器逃逸風險 | PSA `restricted` |
| 忽略 SIGTERM | 發版時請求中斷、資料遺失 | graceful shutdown + `preStop` |
| 用 `kubectl edit` 修改正式環境 | 和 Git 不一致、無法追溯 | GitOps + `selfHeal` |
| 一個超大叢集放所有環境 | 爆炸半徑大、升級風險高 | 依環境／法規等級拆分叢集 |
| 持續使用已退役元件 | 未修補漏洞（Ingress NGINX、Dashboard、Promtail） | 定期盤點、排入遷移計畫 |
| 版本長期停在 EOL | 無安全更新、雲端延長支援費 | 升級納入年度計畫 |
| Webhook `failurePolicy: Fail` 且沒有排除系統 Namespace | Webhook 故障時連 kube-system 都無法建立 Pod | `namespaceSelector` 排除、優先用 VAP／MAP |

#### 14.2.2 實際踩雷案例

| 案例 | 現象 | 根因 | 改善 |
| --- | --- | --- | --- |
| 升級到 1.35 後部分 Node NotReady | kubelet 啟動失敗 | 舊 OS 仍是 cgroup v1 | 升級 OS；升級前執行 11.4.2 檢查 |
| 發版時出現大量 502 | 每次滾動都有少量錯誤 | 沒有 `preStop`，Pod 收到 SIGTERM 時 LB 還在送流量 | 加上 `preStop.sleep` + graceful shutdown |
| 憑證過期導致叢集無法管理 | kubectl 全部 401／x509 錯誤 | 叢集一年沒有升級，也沒有到期告警 | 憑證告警 + 定期升級（升級會自動更新憑證） |
| HPA 擴容後無法縮回 | 副本一直維持最大值 | 以 Memory 使用率擴展 JVM 服務 | 改用 CPU／RPS 指標 |
| etcd 變唯讀 | 所有寫入失敗 | 大量 Event 與過大的 ConfigMap 撐爆 etcd 配額 | 調整配額、defrag、清理、監控 DB 大小 |
| DNS 查詢暴增 | CoreDNS CPU 飆高、外部 API 延遲 | `ndots:5` 造成每次查詢放大 | 調整 `ndots`、啟用 NodeLocal DNSCache |

---

### 14.3 企業環境實務建議

#### 14.3.1 金融業特殊考量

| 需求 | 建議做法 | 章節 |
| --- | --- | --- |
| **資料保護** | KMS v2（HSM）、PV 加密、TLS／mTLS 全程加密 | 8.6、8.7 |
| **稽核日誌** | API Server Audit Log 送 SIEM，依法規保留；exec／RBAC 變更完整記錄 | 8.9 |
| **存取控制** | OIDC + MFA、正式環境 just-in-time 權限、break-glass 帳號封存 | 8.1、7.3 |
| **網路隔離** | default-deny NetworkPolicy、Egress 白名單、Service Mesh mTLS | 4.9、8.8 |
| **合規基準** | CIS Benchmark、PSA `restricted`、VAP／Kyverno 政策 | 8.4、8.5、8.11 |
| **變更管理** | GitOps + MR 雙人審核 + 變更單號寫入 `change-cause` | 12.7 |
| **災難復原** | 多叢集、跨機房；RPO／RTO 定義並定期演練 | 10.5 |
| **供應鏈** | 內部 Registry、簽章驗證、SBOM 保存 | 8.10 |
| **職責分離** | 平台團隊（叢集、Gateway、政策）與應用團隊（Route、Deployment）權限分離 | 4.7、8.2 |

#### 14.3.2 法規與控制對照（參考）

| 控制目標 | Kubernetes 實作 | 證據 |
| --- | --- | --- |
| 存取管理與最小權限 | OIDC、RBAC 群組授權、定期權限盤點 | RoleBinding 清單、權限審查紀錄 |
| 資料加密 | KMS v2、TLS、StorageClass 加密 | EncryptionConfiguration、憑證清單 |
| 日誌與監控 | Audit Log、集中日誌、告警 | SIEM 保存紀錄、告警處理紀錄 |
| 變更管理 | GitOps、MR 審核 | Git 歷史、MR 核准紀錄 |
| 弱點管理 | 映像掃描、Node OS 修補、定期升級 | 掃描報告、升級紀錄 |
| 營運持續 | 多副本、多可用區、DR 演練 | 演練報告、RPO／RTO 實測值 |

> 📌 實際適用的法規（例如金融監理機關的資訊安全規範、ISO 27001、PCI DSS）請由資安與法遵單位確認；上表提供技術控制面的對應參考。

#### 14.3.3 平台工程（Platform Engineering）建議

| 層次 | 建議 |
| --- | --- |
| 黃金路徑（Golden Path） | 提供標準 chart／範本、CI 範本、Namespace 自助申請，讓「正確的做法」也是「最簡單的做法」 |
| 開發者入口 | Backstage 等 IDP，整合服務目錄、文件、範本 |
| 政策即程式碼 | VAP／Kyverno 把規範自動化，先 Warn 再 Deny |
| 成本可視化 | OpenCost／Kubecost 依 Namespace／團隊標籤分攤 |
| 平台 SLO | 平台本身也要定義 SLO（API 可用性、部署成功率、Gateway 延遲） |

---

### 14.4 💡 本章實務建議

1. **把本章的範本做成企業標準 chart**，並以政策強制最低要求。
2. **定期盤點反模式**：用 Kyverno／Trivy Operator 報表找出沒有 request、使用 latest、root 執行的工作負載。
3. **金融業以「稽核證據」為導向設計平台**：每項控制都要能產出證據。
4. **平台團隊以產品思維經營**，降低應用團隊使用 Kubernetes 的認知負擔。

---

## 15. 疑難排解手冊

> 🆕 **v2.0 新增章節**：v1.0 的除錯內容集中在 4.5 節且只有幾個情境。本章依「症狀」整理，每個情境都有判讀方式與處理步驟。

### 15.1 故障排查總流程

```mermaid
flowchart TD
    A["發現問題<br/>告警 / 使用者回報"] --> B{"影響範圍？"}
    B -->|整個叢集| C["Control Plane<br/>/readyz、etcd、憑證"]
    B -->|部分 Node| D["Node<br/>kubelet、Runtime、資源壓力"]
    B -->|單一服務| E{"Pod 狀態？"}
    E -->|Pending| F["15.2 排程問題"]
    E -->|CrashLoopBackOff| G["15.3 啟動失敗"]
    E -->|ImagePullBackOff| H["15.4 映像問題"]
    E -->|OOMKilled| I["15.5 記憶體"]
    E -->|Running 但異常| J["15.6 網路 / 15.7 DNS"]
    E -->|ContainerCreating| K["15.8 儲存 / CNI"]
```

**萬用的第一步**：

```bash
kubectl get pods -n <ns> -o wide
kubectl describe pod <pod> -n <ns>          # 看最下方 Events 與容器 State/Last State
kubectl events -n <ns> --for pod/<pod>
kubectl logs <pod> -n <ns> --all-containers --previous
```

---

### 15.2 Pod 停在 Pending

| Events 訊息 | 原因 | 處理 |
| --- | --- | --- |
| `0/10 nodes are available: 10 Insufficient cpu` | request 超過所有 Node 的可分配量 | 降低 request、擴充 Node、確認 Cluster Autoscaler |
| `node(s) had untolerated taint` | Node 有污點，Pod 沒有對應的容忍 | 加 toleration，或確認是否排錯 Node Pool |
| `node(s) didn't match Pod's node affinity/selector` | nodeSelector／affinity 條件不符 | 檢查 Node 標籤 |
| `didn't match pod topology spread constraints` | `DoNotSchedule` 無法滿足 | 改為 `ScheduleAnyway` 或增加 Node |
| `pod has unbound immediate PersistentVolumeClaims` | PVC 尚未綁定 | 15.8 |
| `exceeded quota` | 超過 ResourceQuota（Pod 根本不會建立，看 ReplicaSet 的 Events） | `kubectl describe quota`，調整配額 |
| Pod 有 `schedulingGates` | 等待外部控制器（例如 Kueue） | 檢查對應控制器 |

```bash
kubectl describe rs -n <ns> -l app.kubernetes.io/name=<app>    # Quota 錯誤會出現在 ReplicaSet
kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints
```

---

### 15.3 CrashLoopBackOff（反覆重啟）

| 判讀 | 可能原因 | 處理 |
| --- | --- | --- |
| `Last State: Terminated, Reason: Error, Exit Code: 1` | 應用啟動失敗（設定錯誤、連不到相依服務） | `kubectl logs --previous` 看錯誤 |
| `Exit Code: 137` + `Reason: OOMKilled` | 記憶體超過 limit | 15.5 |
| `Exit Code: 137` 但不是 OOMKilled | 被 SIGKILL（Liveness 失敗、超過 grace period） | 檢查 Probe 設定與 Events 中的 `Unhealthy` |
| `Exit Code: 126／127` | 指令不存在或無法執行 | 檢查 `command`／映像內容 |
| `Exit Code: 0` 但一直重啟 | 程式正常結束，但 `restartPolicy: Always` | 應用應該持續執行，或改用 Job |
| 日誌出現 `permission denied`、`read-only file system` | `readOnlyRootFilesystem` 或非 root 權限 | 掛載 `emptyDir` 到需要寫入的路徑 |

```bash
# 取得上一次結束的原因與代碼
kubectl get pod <pod> -n <ns> -o jsonpath='{range .status.containerStatuses[*]}{.name}{" "}{.lastState.terminated.reason}{" "}{.lastState.terminated.exitCode}{"\n"}{end}'

# 容器一啟動就掛，無法 exec：複製 Pod 並改成 sleep 進去檢查
kubectl debug pod/<pod> -n <ns> -it --copy-to=<pod>-debug --container=<container> -- sh
```

---

### 15.4 ImagePullBackOff／ErrImagePull

| 訊息 | 原因 | 處理 |
| --- | --- | --- |
| `manifest unknown`／`not found` | tag 或 digest 不存在 | 確認映像名稱與 tag |
| `unauthorized`／`401` | 沒有或錯誤的 `imagePullSecrets` | 檢查 Secret 與 ServiceAccount |
| `toomanyrequests` | Docker Hub 等公有 Registry 限流 | 改用企業 Registry／proxy cache |
| `x509: certificate signed by unknown authority` | 私有 Registry 使用企業 CA | 在 containerd `certs.d` 設定 CA |
| `i/o timeout` | 網路／Proxy／防火牆 | 從 Node 用 `crictl pull` 測試 |
| 映像來自 `docker.io/bitnami/*` | Bitnami 已下架免費版本化映像 | 改用官方或企業自建映像 |

```bash
# 在 Node 上直接測試拉取
sudo crictl pull registry.example.com/ecommerce/order-service:1.4.2
kubectl get secret regcred -n <ns> -o jsonpath='{.data.\.dockerconfigjson}' | base64 -d | jq '.auths | keys'
```

---

### 15.5 OOMKilled 與記憶體問題

| 情境 | 判讀 | 處理 |
| --- | --- | --- |
| 容器 OOMKilled | `Last State: OOMKilled`，超過自己的 memory limit | 調高 limit（同時調 request）或修正記憶體洩漏 |
| Pod 被驅逐（Evicted） | `Reason: Evicted`，訊息為 `The node was low on resource: memory` | Node 記憶體壓力；檢查 Burstable／BestEffort Pod、系統保留 |
| JVM 應用頻繁 OOM | heap 依 limit 計算，加上 Metaspace、執行緒、Direct Memory 超過 limit | `MaxRAMPercentage=75` 以下，保留非 heap 空間 |

```bash
kubectl top pod <pod> -n <ns> --containers
kubectl get pods -A --field-selector=status.phase=Failed -o wide | grep Evicted
kubectl describe node <node> | grep -A 5 Conditions
```

---

### 15.6 網路與 Service 問題

```bash
# 1. Service 是否有後端（沒有 EndpointSlice 端點 = selector 不符或 Pod 未 Ready）
kubectl get endpointslices -n <ns> -l kubernetes.io/service-name=<svc>
kubectl get pods -n <ns> -l <service 的 selector> -o wide

# 2. 從同一 Namespace 測試（臨時容器共享 Pod 網路）
kubectl debug -it pod/<client-pod> -n <ns> --image=nicolaka/netshoot:v0.16 -- \
  curl -sv http://<svc>.<ns>.svc.cluster.local:<port>/actuator/health

# 3. NetworkPolicy 是否擋住
kubectl get networkpolicy -n <ns>
# Cilium 可用 hubble observe 看被丟棄的封包
hubble observe --namespace <ns> --verdict DROPPED
```

| 症狀 | 常見原因 |
| --- | --- |
| Service 沒有 Endpoint | selector 和 Pod 標籤不符、Pod 沒有 Ready、`targetPort` 名稱錯誤 |
| 連線逾時 | NetworkPolicy 拒絕、CNI 故障、安全群組 |
| 間歇性失敗 | 部分 Pod 不健康但 readiness 太寬鬆、conntrack 表滿 |
| Gateway 回 404／503 | HTTPRoute 未附掛（看 `status.parents` 的 `Accepted`／`ResolvedRefs`）、缺少 ReferenceGrant |

```bash
# Gateway API 狀態判讀
kubectl get gateway -A
kubectl describe httproute order-api -n order-prod      # 檢查 Accepted / ResolvedRefs conditions
```

---

### 15.7 DNS 問題

```bash
kubectl debug -it pod/<pod> -n <ns> --image=nicolaka/netshoot:v0.16 -- sh -c '
  cat /etc/resolv.conf
  dig +search order-service
  dig order-service.order-prod.svc.cluster.local
  dig www.example.com'

kubectl -n kube-system get pods -l k8s-app=kube-dns
kubectl -n kube-system logs -l k8s-app=kube-dns --tail=50
```

| 症狀 | 原因 | 處理 |
| --- | --- | --- |
| 叢集內名稱解析失敗 | CoreDNS 異常、NetworkPolicy 沒放行 53 | 4.9 的 DNS 放行政策 |
| 外部名稱很慢 | `ndots:5` 造成多次查詢 | 調整 `ndots` 或使用 FQDN |
| 間歇性 5 秒延遲 | conntrack race（UDP） | NodeLocal DNSCache、`single-request-reopen` |
| CoreDNS CrashLoop（loop detected） | Node 的 resolv.conf 指向本機 | kubelet `resolvConf` 指向真正的上游 |

---

### 15.8 儲存與 Volume 問題

| 症狀 | 原因 | 處理 |
| --- | --- | --- |
| PVC 一直 `Pending` | 沒有預設 StorageClass、CSI 驅動異常、`WaitForFirstConsumer` 正在等 Pod | `kubectl describe pvc`；檢查 CSI controller 日誌 |
| Pod 卡在 `ContainerCreating`，`FailedAttachVolume` | 磁碟仍掛在舊 Node（RWO） | 確認舊 Pod 已刪除；等待 6 分鐘強制卸載或處理 VolumeAttachment |
| `FailedMount ... permission denied` | fsGroup／SELinux 標籤 | 設定 `fsGroup`、`fsGroupChangePolicy: OnRootMismatch` |
| 跨可用區無法掛載 | 磁碟和 Pod 不在同一區 | StorageClass 使用 `WaitForFirstConsumer` |

```bash
kubectl describe pvc <pvc> -n <ns>
kubectl get volumeattachment | grep <pv-name>
kubectl -n kube-system logs -l app=ebs-csi-controller -c csi-provisioner --tail=50
```

---

### 15.9 Node NotReady

```bash
kubectl describe node <node>        # 看 Conditions：Ready、MemoryPressure、DiskPressure、PIDPressure、NetworkUnavailable

# 在 Node 上（或 kubectl debug node/<node>）
sudo systemctl status kubelet containerd
sudo journalctl -u kubelet --since "30 min ago" | tail -50
sudo crictl ps -a | head
df -h /var/lib/containerd /var/lib/kubelet
```

| kubelet 日誌關鍵字 | 原因 |
| --- | --- |
| `cgroup v1` | 1.35+ 在 cgroup v1 主機上 |
| `container runtime is down`、`connection refused ... containerd.sock` | containerd 停止或設定錯誤 |
| `network plugin is not ready` | CNI 未就緒 |
| `x509: certificate has expired` | kubelet 憑證過期（輪替失敗） |
| `PLEG is not healthy` | Runtime 回應過慢（磁碟 IO、過多容器） |
| `failed to run Kubelet: running with swap on` | 主機開啟 swap 但 `failSwapOn: true` |

---

### 15.10 Control Plane 與憑證問題

| 症狀 | 檢查 | 處理 |
| --- | --- | --- |
| `kubectl` 回應 `x509: certificate has expired` | `kubeadm certs check-expiration` | 10.3 更新憑證並重啟 static Pod |
| API Server 很慢、逾時 | API 延遲指標、etcd fsync 延遲、大量 list 請求 | 找出高頻用戶端（audit log）、調整 APF、檢查 etcd 磁碟 |
| `etcdserver: mvcc: database space exceeded` | `etcdctl endpoint status -w table` | compact + defrag + `alarm disarm`，再調整配額 |
| `Internal error occurred: failed calling webhook` | Webhook Pod 狀態 | 修復 Webhook；緊急時暫時調整 `failurePolicy` |
| 資源卡在 `Terminating` | `metadata.finalizers` | 找出負責的控制器並修復；最後手段才移除 finalizer |

```bash
# etcd 健康狀態（在 Control Plane 上）
sudo etcdctl endpoint status --cluster -w table \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# API Server 的 Priority & Fairness 狀態（找出被節流的請求）
kubectl get --raw /debug/api_priority_and_fairness/dump_priority_levels
```

---

### 15.11 💡 本章實務建議

1. **先看 Events 和容器 Last State**，八成問題可以從 `kubectl describe` 得到答案。
2. **把本章做成值班 Runbook**，告警訊息直接附上對應連結（`runbook_url`）。
3. **除錯工具映像預先放進企業 Registry**（netshoot 等），避免故障時才發現拉不到映像。
4. **Events 匯出保存**，事後檢討時才有依據。

---

## 16. Kubernetes 1.29 → 1.37 版本演進

> 🆕 **v2.0 新增章節**：v1.0 以 1.29 為基準。本章整理 1.29 到 1.37 之間與企業維運最相關的變化，方便從舊版叢集規劃升級與教育訓練。成熟度依 Kubernetes 官方 feature gate 文件與各版發布公告（查證日期 2026-10-01）。

### 16.1 各版本重點總覽

| 版本 | 發布 | 主題重點（GA 與重大變更） |
| --- | --- | --- |
| **1.29** | 2023-12 | KMS v2 GA、ReadWriteOncePod GA；nftables kube-proxy Alpha；原生 Sidecar Beta |
| **1.30** | 2024-04 | ValidatingAdmissionPolicy GA、Pod Scheduling Readiness GA、舊式 SA Token 自動清理 GA；結構化認證 Beta |
| **1.31** | 2024-08 | AppArmor 欄位 GA、Job `podFailurePolicy` GA、PDB `unhealthyPodEvictionPolicy` GA；in-tree 雲端供應商程式碼移除；cgroup v1 進入維護模式 |
| **1.32** | 2024-12 | Memory Manager GA；`flowcontrol.apiserver.k8s.io/v1beta3` 停止提供；Pod 層級資源 Alpha |
| **1.33** | 2025-04 | **原生 Sidecar GA**、**nftables kube-proxy GA**、Job `successPolicy`／`backoffLimitPerIndex` GA、`trafficDistribution` GA；**Endpoints API 棄用**；In-place resize Beta |
| **1.34** | 2025-08 | **DRA 核心 GA**、**Node Swap GA**、結構化認證 GA、依 selector 授權 GA、`preStop` sleep 動作 GA、Ordered Namespace Deletion GA、cgroup driver 自動偵測 GA、API Server／kubelet tracing GA；Pod 層級資源、`.kuberc`、MAP Beta |
| **1.35** | 2025-12 | **In-place Pod resize GA**、`PreferSameZone／PreferSameNode` GA、Job `managedBy` GA；**cgroup v1 預設拒絕啟動**、**ipvs 棄用**、最後支援 containerd 1.x；KYAML、Pod 憑證、User Namespaces、容器重啟規則 Beta |
| **1.36** | 2026-04 | **細粒度 kubelet 授權 GA**、**MutatingAdmissionPolicy GA**、**User Namespaces GA**、Image Volume GA、VolumeGroupSnapshot GA、外部 SA Token 簽署 GA、PSI 指標 GA、Node log query GA；**需要 containerd 2.x**、**`gitRepo` 停用**、**`externalIPs` 棄用**；Ingress NGINX 退役（2026-03-24） |
| **1.37** | 2026-08 | **KYAML GA**、**metrics.k8s.io GA**、**Pod 憑證與 ClusterTrustBundle GA**、Storage Version Migrator GA、SELinuxMount GA、HPA 容忍度 GA、`PodReadyToStartContainers` GA；HPA scale-to-zero、Memory QoS、Manifest-based admission、Native Histograms、Gang scheduling Beta；**kube-dns 棄用**、static Pod 禁止引用 Secret／ConfigMap |

### 16.2 依主題整理的演進

#### 16.2.1 工作負載

| 功能 | 演進 | 對本手冊的影響 |
| --- | --- | --- |
| 原生 Sidecar | 1.28 Alpha → 1.29 Beta → **1.33 GA** | 3.6：sidecar 一律使用 `restartPolicy: Always` 的 init 容器 |
| In-place resize | 1.27 Alpha → 1.33 Beta → **1.35 GA** | 6.1.6 |
| Pod 層級資源 | 1.32 Alpha → 1.34 Beta | 6.1.5 |
| 容器重啟規則 | 1.34 Alpha → 1.35 Beta | 3.6.1 |
| Job 失敗／成功政策 | `podFailurePolicy` 1.31 GA；`successPolicy`、`backoffLimitPerIndex` 1.33 GA；`podReplacementPolicy` 1.34 GA | 3.5.2 |
| StatefulSet `maxUnavailable` | 1.35 Beta → 1.37 重新預設開啟 | 3.4 |
| `preStop` sleep | 1.29 Alpha → **1.34 GA** | 3.3、13.5 |

#### 16.2.2 網路

| 功能 | 演進 | 影響 |
| --- | --- | --- |
| kube-proxy nftables | 1.29 Alpha → **1.33 GA** | 4.4：新叢集建議 |
| kube-proxy ipvs | **1.35 棄用** → 預計 1.40 預設停用、1.43 移除 | 4.4 |
| Endpoints API | **1.33 棄用** | 4.3、13.1 改用 EndpointSlice |
| trafficDistribution | 1.33 GA；`PreferSameZone／PreferSameNode` 1.35 GA | 4.2.2 |
| Service `externalIPs` | **1.36 棄用**，預計 1.43 移除 | 4.2.3 |
| Ingress NGINX | 2025-11 宣布、**2026-03-24 退役** | 4.6–4.8 |
| Gateway API | v1.0（2023-10）→ v1.5（ListenerSet、TLSRoute、CORS Standard）→ **v1.6**（TCPRoute／UDPRoute Standard） | 4.7 |
| kube-dns | **1.37 棄用** | 4.5 |

#### 16.2.3 Node 與 Runtime

| 功能 | 演進 | 影響 |
| --- | --- | --- |
| cgroup v1 | 1.31 維護模式 → **1.35 預設拒絕啟動** → 未來移除 | 2.2.2、11.4.2 |
| containerd 1.x | **1.35 為最後支援版本**，1.36 需 2.0+ | 2.3.1 |
| cgroup driver 自動偵測 | **1.34 GA**；1.36 起不再後備使用設定值 | 2.3.1 |
| Node Swap | **1.34 GA** | 2.2.2 |
| User Namespaces | 1.30 Beta → **1.36 GA** | 8.4.3 |
| Image Volume | 1.31 Alpha → **1.36 GA** | 5.3.1 |
| `gitRepo` Volume | **1.36 永久停用** | 5.3 |
| PSI 指標 | 1.33 Alpha → **1.36 GA** | 9.2.4 |

#### 16.2.4 安全

| 功能 | 演進 | 影響 |
| --- | --- | --- |
| KMS v2 | **1.29 GA** | 8.6 |
| ValidatingAdmissionPolicy | **1.30 GA** | 8.5.1 |
| MutatingAdmissionPolicy | 1.30 Alpha → 1.34 Beta → **1.36 GA** | 8.5.2 |
| 結構化認證 | 1.29 Alpha → 1.30 Beta → **1.34 GA** | 8.1.2 |
| 匿名存取限定端點 | **1.34 GA** | 8.1.2 |
| 細粒度 kubelet 授權 | 1.32 Alpha → 1.33 Beta → **1.36 GA** | 8.2.4 |
| 受限身分代理 | 1.35 Alpha → 1.36 Beta | 8.2.4 |
| 外部 SA Token 簽署 | 1.32 Alpha → 1.34 Beta → **1.36 GA** | 8.3 |
| Pod 憑證、ClusterTrustBundle | **1.37 GA** | 8.7 |
| Manifest-based admission | 1.36 Alpha → **1.37 Beta** | 8.5 |
| restricted 禁止 Probe `host` | **1.34** | 6.2.2 |

#### 16.2.5 儲存

| 功能 | 演進 | 影響 |
| --- | --- | --- |
| ReadWriteOncePod | **1.29 GA** | 5.4.3 |
| VolumeAttributesClass | 1.29 Alpha → **1.34 GA** | 5.4.5 |
| 擴容失敗復原 | **1.34 GA** | 5.4.4 |
| VolumeGroupSnapshot | 1.27 Alpha → **1.36 GA**（`groupsnapshot.storage.k8s.io/v1`） | 5.5 |
| PVC Unused condition | 1.36 Alpha → **1.37 Beta** | 5.4.6 |

#### 16.2.6 自動擴縮與排程

| 功能 | 演進 | 影響 |
| --- | --- | --- |
| HPA 自訂容忍度 | 1.33 Alpha → 1.35 Beta → **1.37 GA** | 6.4.1 |
| HPA 縮到 0 | 長期 Alpha → **1.37 Beta（預設開啟）** | 6.4.2 |
| DRA | **1.34 核心 GA**，1.35–1.37 持續擴充 | 6.5 |
| Gang scheduling／Workload-aware scheduling | 1.35 Alpha → 1.37 Beta | 適用 AI/ML 批次 |

#### 16.2.7 工具與可觀測性

| 功能 | 演進 | 影響 |
| --- | --- | --- |
| `.kuberc` | 1.33 Alpha → 1.34 Beta | 7.2 |
| KYAML | 1.34 Alpha → 1.35 Beta → **1.37 GA** | 7.1.2 |
| metrics.k8s.io | Beta 約九年 → **1.37 GA（v1）** | 9.2.1 |
| API Server／kubelet tracing | **1.34 GA** | 9.4 |
| Native Histograms | 1.36 Alpha → **1.37 Beta** | 9.2.4 |
| Kubernetes Dashboard | 封存，改用 Headlamp | 9.6 |
| Helm | **Helm 4（2025-11）**；Helm 3 安全修正至 2027-02-10 | 12.4 |

### 16.3 從 1.29 升級到 1.37 的建議路徑

```mermaid
flowchart LR
    A["1.29（EOL）"] --> B["1.30"] --> C["1.31"] --> D["1.32"] --> E["1.33"]
    E --> F["1.34<br/>先完成 cgroup v2"]
    F --> G["1.35<br/>先完成 containerd 2.x"]
    G --> H["1.36<br/>移除 gitRepo / externalIPs"]
    H --> I["1.37"]
```

| 階段 | 前置工作 |
| --- | --- |
| 升級前（任何版本） | 盤點：OS 是否 cgroup v2、containerd 版本、Ingress NGINX、Dashboard、Endpoints／externalIPs／gitRepo 用量 |
| 1.29 → 1.33 | Control Plane 逐版升級；kubelet 可以每三版升一次（skew 3） |
| 1.33 → 1.34 | 檢查 Endpoints 使用者（警告）；開始規劃 nftables |
| 1.34 → 1.35 | **所有 Node 必須是 cgroup v2** |
| 1.35 → 1.36 | **所有 Node 必須是 containerd 2.0+**；移除 `gitRepo` |
| 1.36 → 1.37 | 檢查 static Pod 是否引用 Secret／ConfigMap；規劃 kube-dns 遷移 |

> 📌 若叢集落後太多（例如仍在 1.29），**建立新叢集並遷移工作負載**（藍綠叢集）通常比連續原地升級 8 次更安全、更快。GitOps 讓這種遷移變得可行。

### 16.4 💡 本章實務建議

1. **以本章作為新版本教育訓練教材**，每次升級前更新一次。
2. **把「行為變更」列入升級檢查清單**：cgroup v2、containerd 2.x、Endpoints、externalIPs、gitRepo、kube-dns。
3. **落後超過 3 個版本的叢集優先考慮藍綠叢集遷移**。
4. **追蹤 1.38（預計 2026-12）的棄用公告**，提前規劃。

---

## 附錄 A：檢查清單（Checklist）

### A.1 新服務部署檢查清單

**部署前**

- [ ] 映像來自企業 Registry，以語意版本 + digest 指定，已通過掃描並簽章
- [ ] Deployment 設定完整
  - [ ] `replicas` ≥ 3（關鍵服務）並設定拓撲分散
  - [ ] 每個容器都有 request 與 memory limit
  - [ ] Startup／Liveness／Readiness Probe 分工正確
  - [ ] `securityContext` 符合 `restricted`（non-root、drop ALL、唯讀根目錄、seccomp）
  - [ ] `preStop.sleep` 與 `terminationGracePeriodSeconds` 已設定，應用支援 graceful shutdown
  - [ ] 使用 `app.kubernetes.io/*` 建議標籤
- [ ] Service 使用具名埠與 `appProtocol`
- [ ] HTTPRoute（或 Ingress）已設定，並取得平台團隊授權附掛 Gateway
- [ ] ConfigMap 已建立；Secret 透過 ExternalSecret 取得
- [ ] PodDisruptionBudget（`maxUnavailable: 1`）
- [ ] HPA（如需要）
- [ ] NetworkPolicy 已放行必要流量（含 DNS）
- [ ] ServiceMonitor 與 PrometheusRule 已建立
- [ ] 所有物件已提交到設定 Repo，透過 GitOps 部署

**部署後**

- [ ] Pod 全部 Running 且 Ready，沒有反覆重啟
- [ ] Service 有 EndpointSlice 端點
- [ ] HTTPRoute `Accepted`／`ResolvedRefs` 為 True，可從外部存取
- [ ] 日誌以 JSON 格式輸出並出現在日誌平台
- [ ] 指標出現在 Prometheus，告警規則生效
- [ ] 追蹤資料可在 APM／Tempo 查到
- [ ] 進行一次滾動重啟，確認零停機

### A.2 日常維運檢查清單

**每日**

- [ ] 所有 Node Ready，沒有 MemoryPressure／DiskPressure
- [ ] `kube-system` 與平台元件正常
- [ ] 檢查 CrashLoopBackOff、OOMKilled、Evicted 的 Pod
- [ ] 檢查告警與 Warning Events
- [ ] etcd 備份成功

**每週**

- [ ] 檢查憑證到期日（Control Plane、kubelet、cert-manager）
- [ ] 檢查 PVC 使用率與 `Unused` PVC
- [ ] 檢查映像掃描新發現的 CVE
- [ ] 檢查 etcd 資料庫大小與 fsync 延遲
- [ ] 清理無用映像與已完成的 Job

**每月**

- [ ] 檢查 Kubernetes 與附加元件的新版本、安全公告
- [ ] 審查 RBAC 權限與高風險權限
- [ ] 審查 ResourceQuota 與實際使用量（成本）
- [ ] 檢查棄用 API 使用量（`apiserver_requested_deprecated_apis`）
- [ ] 檢查是否仍使用已退役元件（Ingress NGINX、Dashboard、Promtail、kube-dns）

**每季**

- [ ] etcd 還原演練
- [ ] 災難復原（DR）演練
- [ ] 升級測試叢集到下一個 minor 版本

### A.3 升級前檢查清單

完整清單見 [11.8 升級前檢查清單](#118-升級前檢查清單)。摘要如下：

- [ ] 閱讀 Release Notes 與 Urgent Upgrade Notes
- [ ] 確認升級路徑（Control Plane 逐版）
- [ ] cgroup v2、containerd 2.x、gitRepo、externalIPs、kube-proxy 模式檢查
- [ ] 棄用 API 檢查
- [ ] 附加元件相容性確認
- [ ] 備份 etcd 與 PKI
- [ ] PDB 允許中斷
- [ ] 測試叢集演練
- [ ] 維護窗口與通知

### A.4 安全基準檢查清單

- [ ] 人員以 OIDC 登入，admin.conf 封存
- [ ] 匿名存取只允許健康檢查端點
- [ ] 應用 Namespace 皆為 PSA `restricted`
- [ ] 每個 Namespace 都有 default-deny NetworkPolicy
- [ ] Secret 以 KMS v2 加密，不存在 Git 中
- [ ] Audit Log 送到外部 SIEM
- [ ] 監控工具沒有 `nodes/proxy` 權限
- [ ] 只允許企業 Registry 且已簽章的映像
- [ ] 定期執行 kube-bench（CIS Benchmark）

---

## 附錄 B：常見問答（Q&A）

**Q1：我們還在 1.29／1.30，要直接跳到 1.37 嗎？**
Control Plane 不能跳版，必須逐版升級。落後很多時，建議建立 1.37 新叢集並以 GitOps 遷移工作負載（藍綠叢集），通常比連續升級更快、風險更低。見 [16.3](#163-從-129-升級到-137-的建議路徑)。

**Q2：Ingress NGINX 已經退役，現有服務會馬上壞掉嗎？**
不會。既有部署仍能運作，映像與 chart 也仍可下載，但不會再有任何安全修補。請列入資安風險並排入遷移計畫：優先遷移到 Gateway API，短期可改用 F5 NGINX Ingress Controller 等仍維護的 Controller。見 [4.6.2](#462-ingress-nginx-退役說明重要)。

**Q3：Gateway API 已經可以用在正式環境了嗎？**
可以。核心資源（Gateway、HTTPRoute、GRPCRoute、ReferenceGrant 等）都是 `v1`，主流實作皆通過 conformance。重點是選擇支援你所需 Extended 功能的實作，並只安裝 Standard channel CRD。

**Q4：CPU limit 到底要不要設？**
延遲敏感的線上服務通常不設 CPU limit（避免 CFS 節流），只設 request；需要可預測效能或多租戶隔離時才設。記憶體則一律 limit = request。見 [6.1.3](#613-qos-等級與-cpu-limit-的取捨)。

**Q5：Swap 現在可以開了嗎？**
1.34 起 Node Swap 已 GA，但需要明確設定 `failSwapOn: false` 與 `LimitedSwap`，而且只有 Burstable Pod 會使用。多數企業叢集維持關閉即可；記憶體密集且可接受效能波動的工作負載才考慮。見 [2.2.2](#222-作業系統需求)。

**Q6：升級到 1.35 後 kubelet 起不來？**
最常見的原因是主機仍是 cgroup v1。用 `stat -fc %T /sys/fs/cgroup/` 確認，升級 OS；緊急時可暫時設定 `failCgroupV1: false`。

**Q7：containerd 1.7 還能用嗎？**
1.35 是最後一個支援 containerd 1.x 的版本，1.36 起必須使用 containerd 2.0 以上。containerd 2.x 的設定檔格式（version 3）與 1.x 不同，升級時要重新產生設定。

**Q8：Secret 用 Base64 存放安全嗎？**
不安全，Base64 只是編碼。要啟用 KMS v2 靜態加密、限制 RBAC，並以 External Secrets 等方式讓 Secret 不進 Git。

**Q9：kubectl 的 `--record` 還能用嗎？**
仍可執行，但已棄用並會顯示警告，未來會移除。請改用 `kubernetes.io/change-cause` 註解或以 Git commit 記錄變更。

**Q10：HPA 能縮到 0 嗎？**
1.37 起 `HPAScaleToZero` Beta 預設開啟，`minReplicas: 0` 搭配至少一個 Object 或 External 指標即可。1.36 以前請使用 KEDA。

**Q11：Helm 3 還能用多久？**
Helm 3 已於 2026-09-09 停止 bug 修正，安全修正到 2027-02-10。請規劃遷移到 Helm 4，並注意新 release 預設改用 Server-Side Apply。

**Q12：PodSecurityPolicy 的替代方案是什麼？**
PSP 已於 1.25 移除。內建以 Pod Security Admission（三個等級）處理，客製規則用 ValidatingAdmissionPolicy、MutatingAdmissionPolicy 或 Kyverno／Gatekeeper。

**Q13：Kubernetes Dashboard 還能用嗎？**
Kubernetes Dashboard 已封存，請改用 Headlamp（Kubernetes SIG UI 專案）或 k9s 等工具。

**Q14：單一叢集要放幾個環境？**
正式與非正式環境建議分開叢集（至少不同 Node Pool 與嚴格隔離）。不同法規等級的系統也建議分叢集，以縮小爆炸半徑並簡化稽核。

---

## 附錄 C：常用指令速查

### C.1 叢集與 Node

| 目的 | 指令 |
| --- | --- |
| 叢集健康 | `kubectl get --raw='/readyz?verbose'` |
| Node 狀態 | `kubectl get nodes -o wide` |
| Node 詳情 | `kubectl describe node <node>` |
| 維護 Node | `kubectl cordon <node>`；`kubectl drain <node> --ignore-daemonsets --delete-emptydir-data` |
| 恢復排程 | `kubectl uncordon <node>` |
| Node 除錯 | `kubectl debug node/<node> -it --image=ubuntu:24.04 --profile=sysadmin` |
| 憑證到期 | `sudo kubeadm certs check-expiration` |
| 升級計畫 | `sudo kubeadm upgrade plan` |

### C.2 工作負載

| 目的 | 指令 |
| --- | --- |
| 套用（SSA） | `kubectl apply --server-side -f <file>` |
| 套用前差異 | `kubectl diff -f <file>` |
| 發佈狀態 | `kubectl rollout status deploy/<name>` |
| 發佈歷史 | `kubectl rollout history deploy/<name>` |
| 回滾 | `kubectl rollout undo deploy/<name> --to-revision=<n>` |
| 重新啟動 | `kubectl rollout restart deploy/<name>` |
| 擴縮 | `kubectl scale deploy/<name> --replicas=<n>` |
| 原地調整資源 | `kubectl patch pod <pod> --subresource resize -p '<json>'` |
| 欄位說明 | `kubectl explain <resource>.<field> --recursive` |
| KYAML 輸出 | `kubectl get <resource> <name> -o kyaml` |

### C.3 除錯

| 目的 | 指令 |
| --- | --- |
| 前一次日誌 | `kubectl logs <pod> --previous` |
| 多容器日誌 | `kubectl logs deploy/<name> --all-containers --prefix` |
| 事件 | `kubectl events -n <ns> --types=Warning` |
| 臨時容器 | `kubectl debug -it pod/<pod> --image=nicolaka/netshoot:v0.16 --target=<container>` |
| 複製 Pod 除錯 | `kubectl debug pod/<pod> -it --copy-to=<new> --container=<c> -- sh` |
| 資源使用 | `kubectl top pods -A --sort-by=memory` |
| 權限檢查 | `kubectl auth can-i <verb> <resource> --as=<user>` |
| 目前身分 | `kubectl auth whoami` |

### C.4 網路與 Gateway

| 目的 | 指令 |
| --- | --- |
| Service 後端 | `kubectl get endpointslices -l kubernetes.io/service-name=<svc>` |
| Gateway 狀態 | `kubectl get gateway -A`；`kubectl describe httproute <name>` |
| kube-proxy 模式 | `kubectl -n kube-system get cm kube-proxy -o jsonpath='{.data.config\.conf}'` |
| 轉換 Ingress | `ingress2gateway print --providers=ingress-nginx -A` |
| 埠轉發 | `kubectl port-forward svc/<svc> 8080:80` |

### C.5 etcd

| 目的 | 指令 |
| --- | --- |
| 快照 | `etcdctl snapshot save <file> --endpoints=... --cacert=... --cert=... --key=...` |
| 驗證快照 | `etcdutl snapshot status <file> -w table` |
| 還原 | `etcdutl snapshot restore <file> --data-dir <dir> ...` |
| 狀態 | `etcdctl endpoint status --cluster -w table` |

---

## 附錄 D：版本紀錄

### D.1 文件版本歷史

| 版本 | 日期 | 說明 |
| --- | --- | --- |
| 1.0 | 2026-01-29 | 初版，8 章，對應 Kubernetes 1.29+ |
| **2.0** | **2026-10-01** | 企業標準技術白皮書版：以 Kubernetes **v1.37.1** 為主線（1.34／1.35 差異註記）；擴充為 16 章 + 附錄 A–F；全面查證並修正 v1.0 內容 |

### D.2 v1.0 → v2.0 更正對照表

| # | 章節 | v1.0 內容 | v2.0 更正 | 依據 |
| --- | --- | --- | --- | --- |
| 1 | 文件資訊 | 對應 Kubernetes 1.29+ | 改為 1.37.1 主線；1.29 已於 2025-02-28 EOL | kubernetes.io releases schedule／EOL 資料 |
| 2 | 1.2.5 | etcd 備份指令加 `ETCDCTL_API=3` | etcd 3.4 起為預設，不需設定；狀態檢查與還原改用 `etcdutl` | etcd CHANGELOG-3.6 |
| 3 | 1.2.3 | kube-proxy「每個 Node 必須有」 | 可由 eBPF CNI 取代；`ipvs` 1.35 棄用；nftables 1.33 GA | 1.35／1.37 發布公告、feature gate |
| 4 | 1.3.2 | sidecar 寫在 `containers`、使用 `fluentd:latest` | 改用原生 Sidecar（1.33 GA）並固定版本 | SidecarContainers feature gate |
| 5 | 1.3.5 | 建議 `version`、`tier` 自訂標籤並放入 selector | 改用 `app.kubernetes.io/*` 建議標籤，版本不放 selector | 官方 Recommended Labels |
| 6 | 1.3.6 | 手動設定 `deployment.kubernetes.io/revision` | 由控制器維護，不應手動設定 | Deployment controller 行為 |
| 7 | 2.1.1 | pkgs.k8s.io repo 路徑為 `v1.29` | 改為 `v1.37`，並說明 minor 升級需切換 repo | kubeadm 安裝文件 |
| 8 | 2.1.3 | AKS「免收 Control Plane 費用」 | 只有 Free tier 不收費且無 SLA；正式環境通常用 Standard tier | 雲端定價說明 |
| 9 | 2.2.2 | 「必須停用 Swap」、Kernel 4.15+ | Swap 1.34 GA 可受控使用；需 cgroup v2（1.35 起預設拒絕 cgroup v1）；nftables 需核心 5.13+ | NodeSwap gate、kernel requirements、1.37 公告 |
| 10 | 2.3.1 | `apt install containerd` + sed 修改 `SystemdCgroup` | 1.36 起需 containerd 2.x；config version 3 路徑為 `io.containerd.cri.v1.runtime`；cgroup driver 1.34 起自動偵測 | containerd v2.4.1 docs/cri/config.md、1.35 公告 |
| 11 | 2.1.1 | CNI 範例使用 Flannel `releases/latest` | 改為 Cilium／Calico 固定版本；Flannel 不支援 NetworkPolicy | 各專案 release |
| 12 | 3.2 | `CrashLoopBackOff` 等被視為 Pod 狀態 | 說明它們是容器狀態，不是 Pod Phase | Pod lifecycle 文件 |
| 13 | 3.3.1 | Deployment 範例缺少安全設定、使用 `initialDelaySeconds` | 加入 `securityContext`、startupProbe、拓撲分散、`preStop.sleep` 等 | PSS、PodLifecycleSleepAction GA 1.34 |
| 14 | 4.2.1 | `aws-load-balancer-type: nlb` 註解寫「ALB 範例」 | NLB 是 L4；改用 AWS LB Controller 的 `external` + `nlb-target-type` | AWS Load Balancer Controller 文件 |
| 15 | 4.6 | 推薦 NGINX Ingress 為最普及選擇 | Ingress NGINX 已於 2026-03-24 退役；改列仍維護的 Controller 與遷移指南 | 1.36 發布公告、ingress-nginx repo archived |
| 16 | 4.6.3 | Kong、Traefik 等 Controller 比較未標註 Gateway API 支援 | 補上 Gateway API 支援與版本 | Gateway API v1.6 conformance |
| 17 | 5.2.2 | `Secret` 安全建議只有四點 | 補充 KMS v2、稽核、映像拉取憑證驗證等完整層次 | KMSv2 GA 1.29、KubeletEnsureSecretPulledImages |
| 18 | 6.1.4 | Java Limit 為 Request 的 1.5–2 倍（含記憶體） | Memory limit = request；CPU limit 依服務性質；JVM 使用 `MaxRAMPercentage` | QoS 與驅逐行為 |
| 19 | 6.2.2 | gRPC Probe 標示「1.24+」 | 1.24 Beta，1.27 GA | GRPCContainerProbe gate |
| 20 | 6.2.2 | Probe HTTP 標頭放 `Authorization: Bearer` | Probe 端點應免認證並只在內部提供；1.34 起 restricted 禁止 Probe `host` | 1.34 發布公告 |
| 21 | 6.4.1 | HPA 範例以 Memory 使用率擴展 Java 服務 | JVM 記憶體難以下降，改用 CPU／RPS；加入 `tolerance`（1.37 GA） | HPAConfigurableTolerance gate |
| 22 | 7.1.1 | 除錯以 `kubectl run debug` 為主 | 改用 `kubectl debug` 與 `--profile` | kubectl debug profiles（v1.37.1 原始碼） |
| 23 | 7.3 | `kubectl debug --copy-to` 標示「1.25+」 | 補充 `--profile` 與權限控管 | 同上 |
| 24 | 7.4 | 未說明 `--record` 狀態 | `--record` 已棄用（仍可用，會出現警告），改用 `change-cause` 註解 | kubectl record_flags.go（v1.37.1） |
| 25 | 9.3.2 | Fluent Bit 掛載 `/var/lib/docker/containers`、使用 `latest` | dockershim 1.24 已移除；改讀 `/var/log/containers`（CRI 格式）並固定版本 | Fluent Bit chart、CRI 日誌格式 |
| 26 | 9.3.3 | JSON 日誌範例以 ```java 標示 | 改為 ```json，並採用 ECS／OTel 欄位 | Markdown 格式 |
| 27 | 8.2.2 | RoleBinding 引用不存在的 Role `service-role` | 補齊 Role 定義 | — |
| 28 | 8.2.2 | 唯讀 ClusterRole 使用 `resources: ["*"]` | 會包含 Secret；改用內建 `view` 或明確列出資源 | RBAC 文件 |
| 29 | 8.4.2 | 未提到 PSP 已移除、AppArmor 欄位 | PSP 1.25 移除；AppArmor 欄位 1.31 GA | AppArmor gate、PSP 移除公告 |
| 30 | 10.1.3 | LimitRange `default.cpu: 500m` | 預設 CPU limit 會造成節流，改為只限制記憶體 | 6.1.3 原則 |
| 31 | 10.3.1 | `kubeadm certs renew all` 後 `systemctl restart kubelet` | 重啟 kubelet 不會重啟 static Pod；需暫移 manifest | kubeadm-certs 文件 |
| 32 | 10.4.3 | 容量規劃比例未說明基準 | 以 request／allocatable 為基準並要求 N+1 | — |
| 33 | 11.1 | 支援約 14 個月、僅相鄰版本升級 | 補上 12+2 個月結構與 1.34–1.37 EOL 日期；Control Plane 不可跳版、kubelet 可落後 3 版 | patch-releases、version-skew-policy |
| 34 | 11.3 | 升級順序把 kubelet 放最後 | 每台 Node 升級時一併升級 kubelet | version-skew-policy |
| 35 | 11.5 | 升級範例未切換 repo、Worker 漏 `apt-mark unhold`、版號 1.29 | 補齊並改為 1.36.5 → 1.37.1 | kubeadm upgrade 文件 |
| 36 | 12.2 | `docker:latest`、`bitnami/kubectl:latest` | Bitnami 免費版本化映像已下架；改用固定版本與 dl.k8s.io 下載 kubectl | Bitnami 公告 |
| 37 | 12.2 | Trivy 指令放在 ```yaml 區塊 | 改為正確的 CI job 與 bash 區塊 | Markdown 格式 |
| 38 | 12.4.4 | values 以 `ingress` 為主 | 改為 Gateway API `route`，加入 PDB、digest | — |
| 39 | 13.1.2 | 使用 `kind: Endpoints` | Endpoints 1.33 起棄用，改用 EndpointSlice | 1.33 Endpoints 棄用公告 |
| 40 | 13.5 | `@PreDestroy` 示範優雅關機、`sh -c "sleep 10"` | 改用 `server.shutdown=graceful` 與原生 `preStop.sleep` | Spring Boot、PodLifecycleSleepAction |
| 41 | 文件格式 | 中繼資料重複、行尾空白不一致；檢查清單包在 ```markdown；裸 code fence；TOC 錨點含 emoji 導致失效 | 中繼資料改為表格；清單改為真正的 `- [ ]`；所有 fence 標註語言；TOC 自動產生並以 Hugo 渲染結果驗證 | Hugo goldmark 標題 ID 規則 |

### D.3 v2.0 新增章節

| 章節 | 內容 |
| --- | --- |
| 1.5 | API 版本與功能成熟度 |
| 2.3.2、2.3.3 | 高可用 Control Plane、CNI 選型 |
| 3.4、3.5、3.6 | StatefulSet、DaemonSet／Job／CronJob、Init 與 Sidecar 容器 |
| 4.1、4.3–4.5、4.7–4.9 | 網路模型、EndpointSlice、kube-proxy 模式、CoreDNS、**Gateway API**、**Ingress NGINX 遷移**、NetworkPolicy |
| 5.3–5.5 | Volume 類型、PV／PVC／StorageClass、快照 |
| 6.1.5、6.1.6、6.3、6.4、6.5 | Pod 層級資源、In-place resize、排程控制、KEDA／VPA／Karpenter、DRA |
| 7.1.3、7.2、7.6 | Server-Side Apply、`.kuberc`、Argo Rollouts |
| 8（全章） | 安全強化 |
| 9.4–9.6 | OpenTelemetry、Events、Headlamp |
| 10.2、10.5 | etcd 還原、Velero 災難復原 |
| 11.2、11.4、11.6 | Version Skew、逐版破壞性變更、Managed 升級 |
| 12.4–12.7 | Helm 4、Kustomize、Argo CD／Flux、環境晉升 |
| 13.3、13.4 | External Secrets Operator、cert-manager |
| 14.1.2、14.3.2、14.3.3 | 企業標準範本、法規控制對照、平台工程 |
| 15（全章） | 疑難排解手冊 |
| 16（全章） | 1.29 → 1.37 版本演進 |
| 附錄 B–F | Q&A、指令速查、版本紀錄、查證紀錄、參考資料 |

---

## 附錄 E：查證紀錄

本版所有版本資訊與功能成熟度於 **2026-10-01** 查證。主要方法：以 `gh api` 讀取 GitHub 上的官方原始碼與文件（kubernetes/kubernetes `v1.37.1` tag、kubernetes/website `main`）、各專案 release；部分資訊以官方網站與公告確認。

| # | 查證項目 | 結果 | 來源 |
| --- | --- | --- | --- |
| 1 | Kubernetes 最新版本 | v1.37.1（2026-09-23）；同日發布 1.36.5、1.35.9、1.34.12 | kubernetes/kubernetes releases |
| 2 | 各版 EOL | 1.37：2027-10-28；1.36：2027-06-28；1.35：2027-02-28；1.34：2026-10-27；1.33 已於 2026-06-28 EOL；1.29 已於 2025-02-28 EOL | kubernetes/website `data/releases/schedule.yaml`、`eol.yaml` |
| 3 | 支援期結構 | 14 個月（12 個月標準 + 2 個月維護模式） | `content/en/releases/patch-releases.md` |
| 4 | Version skew | kubelet／kube-proxy 可舊 3 個 minor；KCM／scheduler 可舊 1 個；kubectl ±1 | `content/en/releases/version-skew-policy.md` |
| 5 | 各功能 GA 版本 | Sidecar 1.33、NodeSwap 1.34、In-place resize 1.35、User Namespaces 1.36、MAP 1.36、Image Volume 1.36、Pod 憑證 1.37、gRPC Probe 1.27、AppArmor 1.31、API Server tracing 1.34 等 | feature-gates 文件（stages 欄位） |
| 6 | kubeadm 1.37 預設元件 | etcd 3.7.0、CoreDNS v1.14.6、pause 3.10.2；最低 kubelet 為 skew −3 | `cmd/kubeadm/app/constants/constants.go`（v1.37.1） |
| 7 | kubeadm 設定 API | v1beta4 為優先版本；原始碼已有 `v1`（開發中） | `cmd/kubeadm/app/apis/kubeadm/scheme/scheme.go`、`v1/doc.go` |
| 8 | kubelet 預設值 | `failCgroupV1` 預設 true；`failSwapOn` 預設 true；`memorySwap.swapBehavior` 支援 `LimitedSwap` | `pkg/kubelet/apis/config/v1beta1/defaults.go`、kubelet types.go |
| 9 | kube-proxy 預設模式 | Linux 未設定時為 `iptables` | `staging/src/k8s.io/kube-proxy/config/v1alpha1/types.go` |
| 10 | kubectl `--record` | 仍存在，已標示棄用（"will be removed in the future"） | `cli-runtime/pkg/genericclioptions/record_flags.go` |
| 11 | kubectl debug profiles | legacy、general、baseline、restricted、netadmin、sysadmin | `kubectl/pkg/cmd/debug/profiles.go` |
| 12 | kubectl 輸出 `kyaml` | `-o kyaml` 已支援 | `cli-runtime/.../json_yaml_flags.go` |
| 13 | `.kuberc` 格式 | `kubectl.config.k8s.io/v1beta1`；`credentialPluginPolicy` 值為 AllowAll／DenyAll／Allowlist | `kubectl/pkg/config/v1beta1/types.go`、kuberc 文件 |
| 14 | containerd 2.x cgroup 設定 | config version 3，`plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc.options` | containerd v2.4.1 `docs/cri/config.md` |
| 15 | etcd 3.6 變更 | 移除 `etcdctl snapshot restore／status`，改用 `etcdutl` | etcd `CHANGELOG-3.6.md` |
| 16 | Endpoints 棄用 | 1.33 起棄用，回傳 Warning | 官方部落格 2025 endpoints-deprecation |
| 17 | Ingress NGINX | 2026-03-24 退役；repo 已封存；最後版本 controller-v1.15.1 | 1.36 發布公告、GitHub repo 狀態 |
| 18 | Gateway API v1.6.2 | Standard channel 含 Gateway／HTTPRoute／GRPCRoute／TLSRoute／TCPRoute／UDPRoute／ListenerSet／BackendTLSPolicy（皆 `v1`）、ReferenceGrant（v1） | `standard-install.yaml`（v1.6.2）解析 |
| 19 | ingress2gateway | v1.2.0；`print --providers=ingress-nginx`；支援 `--emitter`、`-A` | ingress2gateway README（v1.2.0） |
| 20 | Ingress NGINX 遷移陷阱 | regex 前綴且不分大小寫等五項 | 官方部落格〈Before You Migrate〉 |
| 21 | 1.35–1.37 棄用 | ipvs（1.35）、externalIPs（1.36）、gitRepo 停用（1.36）、kube-dns（1.37）、static Pod 引用 Secret（1.37） | 各版發布公告 |
| 22 | 內建 API 移除 | 1.32 之後到 1.37 沒有再移除 | deprecation-guide.md |
| 23 | 生態系版本 | Helm 4.3.0、containerd 2.4.1、etcd 3.7.2、Cilium 1.20.2、Calico 3.32.2、Argo CD 3.5.3、Flux 2.9.5、Fluent Bit 5.1.2、Prometheus 3.15.0、KEDA 2.21.0、Karpenter 1.14.1、Kyverno 1.19.1、Gatekeeper 3.23.1、Trivy 0.74.0、cert-manager 1.21.2、Velero 1.18.4、kind 0.33.0 等 | 各專案 GitHub releases/latest |
| 24 | Helm 3 支援 | bug 修正至 2026-09-09；安全修正至 2027-02-10；Helm 4.0 於 2025-11 發布 | helm.sh 部落格 Helm v3 End of Life |
| 25 | Bitnami | 2025-08-28 起變更；`docker.io/bitnami` 版本化映像移至 `bitnamilegacy` 並停止更新 | 多方公告（Bitnami 目錄變更） |
| 26 | Kubernetes Dashboard、HNC、Kaniko | GitHub repo 皆已封存 | GitHub repo 狀態 |
| 27 | External Secrets Operator | v2.11.0，API `external-secrets.io/v1`，相容性表標示 Kubernetes 1.36 | ESO `stability-support.md` |
| 28 | Velero AWS 外掛 | Velero 1.18.x 對應 velero-plugin-for-aws v1.14.x | velero-plugin-for-aws README |
| 29 | network-policy-api | v0.2.0 將 ANP／BANP 合併為 ClusterNetworkPolicy（v1alpha2） | network-policy-api release notes |

### E.1 待確認項目

| # | 項目 | 說明 |
| --- | --- | --- |
| 1 | kubeadm `v1` 設定 API | 原始碼已有 `kubeadm.k8s.io/v1`，但遷移版本標示為 TODO；待正式公告後再更新 2.1.2 範例 |
| 2 | Storage Version Migrator 成熟度 | 1.37 發布公告列為 GA，但 feature gate 文件仍標示 Beta（1.35）；待文件更新 |
| 3 | ESO 對 Kubernetes 1.37 的支援 | 目前相容性表只列到 1.36，待下一版 ESO 確認 |
| 4 | 雲端代管版本 | GKE／EKS／AKS 目前提供的最新版本與延長支援費率未逐一查證，請以各雲端官方頁面為準 |
| 5 | `registry.k8s.io` 官方 kubectl 映像 | 未能確認是否提供官方 kubectl 容器映像，本版改以 dl.k8s.io 下載二進位檔 |
| 6 | Gateway API 各實作的 Extended 功能支援 | CORS、URLRewrite、BackendTLSPolicy 等支援度依實作而異，導入前需查看 conformance 報告 |
| 7 | Kubernetes 1.38 | 預計 2026-12 發布，屆時需更新第 11、16 章與 cgroup v1 移除時程 |
| 8 | 第三方映像版本 | 範例中的應用映像（nginx 1.30.5、postgres 18.6、node-exporter v1.12.1 等）會持續更新，正式使用前請重新確認 |

---

## 附錄 F：參考資料

### F.1 官方文件與原始碼

- [Kubernetes 官方文件](https://kubernetes.io/docs/)
- [Kubernetes GitHub](https://github.com/kubernetes/kubernetes)
- [Kubernetes Releases（版本與支援期）](https://kubernetes.io/releases/)
- [Version Skew Policy](https://kubernetes.io/releases/version-skew-policy/)
- [Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)
- [Feature Gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
- [Kubernetes Blog：v1.37 Release](https://kubernetes.io/blog/)
- [Kubernetes Enhancement Proposals（KEP）](https://github.com/kubernetes/enhancements)
- [CNCF Landscape](https://landscape.cncf.io/)

### F.2 網路與流量

- [Gateway API](https://gateway-api.sigs.k8s.io/)
- [Gateway API Implementations](https://gateway-api.sigs.k8s.io/implementations/)
- [Ingress NGINX Retirement: What You Need to Know](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)
- [ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway)
- [Cilium](https://docs.cilium.io/)、[Calico](https://docs.tigera.io/calico/latest/about/)
- [Envoy Gateway](https://gateway.envoyproxy.io/)

### F.3 安全

- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes)
- [Kyverno](https://kyverno.io/)、[OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/)
- [Sigstore cosign](https://docs.sigstore.dev/)、[Trivy](https://trivy.dev/)
- [External Secrets Operator](https://external-secrets.io/)、[cert-manager](https://cert-manager.io/)

### F.4 維運、可觀測性與交付

- [etcd 文件](https://etcd.io/docs/)
- [Prometheus](https://prometheus.io/docs/)、[OpenTelemetry](https://opentelemetry.io/docs/)、[Fluent Bit](https://docs.fluentbit.io/)
- [Headlamp](https://headlamp.dev/)
- [Velero](https://velero.io/docs/)
- [Helm](https://helm.sh/docs/)、[Kustomize](https://kubectl.docs.kubernetes.io/)
- [Argo CD](https://argo-cd.readthedocs.io/)、[Flux](https://fluxcd.io/flux/)
- [KEDA](https://keda.sh/)、[Karpenter](https://karpenter.sh/)

### F.5 書籍

- [Kubernetes Patterns（O'Reilly）](https://www.oreilly.com/library/view/kubernetes-patterns/9781492050278/)
