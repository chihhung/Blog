+++
date = '2026-05-19T10:00:00+08:00'
draft = false
title = 'TSD（技術規格文件）範本'
tags = ['範本', '設計開發', '軟體工程']
categories = ['教學']
+++

# TSD（技術規格文件｜Technical Specification Document）範本

> **版本**：1.0  
> **參照標準**：ISO/IEC/IEEE 15288:2023、ISO/IEC 25010:2023、IEEE 1016-2009  
> **適用對象**：資深開發工程師、技術主管、QA 工程師  
> **文件性質**：工程師實作指南與底層技術規格文件

---

## 📋 使用說明

TSD 是工程師的實作指南，詳細說明「**底層技術與程式碼邏輯**」。內容涵蓋類別與函式設計、演算法邏輯、資料結構、錯誤處理機制及自動化測試規劃。

### 何時使用本範本

- 進入開發實作階段前，將 SDD 的設計轉化為可直接編碼的技術規格
- 複雜演算法或業務邏輯需要詳細記錄時
- 技術交接或 Code Review 的參考文件

### 與其他文件的關係

```
PRD（做什麼） → SDD（如何設計） → TSD（如何實作）
     ↑                ↑                ↑
   產品經理          架構師           開發工程師
```

### 填寫原則

1. **可直接編碼**：規格描述需精確到可直接轉換為程式碼
2. **測試可驗證**：每個功能模組需附帶測試策略
3. **錯誤完整**：覆蓋所有已知的錯誤場景與處理方式
4. **效能可量化**：關鍵演算法需標注時間/空間複雜度

---

## 📄 範本正文

---

# [模組/功能名稱] 技術規格文件（TSD）

## 1. 文件資訊

| 項目 | 內容 |
|------|------|
| **文件編號** | TSD-[專案代碼]-[模組代碼]-[序號] |
| **版本** | v0.1 |
| **建立日期** | YYYY-MM-DD |
| **最後更新** | YYYY-MM-DD |
| **撰寫者** | [工程師姓名] |
| **審核者** | [技術主管 / 架構師] |
| **狀態** | 草稿 / 審查中 / 已核准 |

### 版本歷程

| 版本 | 日期 | 修改人 | 修改內容摘要 |
|------|------|--------|-------------|
| v0.1 | YYYY-MM-DD | [姓名] | 初版建立 |

### 關聯文件

| 文件名稱 | 文件編號 | 版本 | 關聯性 |
|---------|---------|------|--------|
| 系統設計文件（SDD） | SDD-XXX-001 | v1.0 | 架構設計 |
| 產品需求文件（PRD） | PRD-XXX-001 | v1.0 | 需求來源 |
| API 規格文件 | API-XXX-001 | v1.0 | 介面規格 |

---

## 2. 技術概述

### 2.1 模組/功能範圍

> 簡述本 TSD 涵蓋的模組或功能範圍，以及與其他模組的邊界。

**模組名稱**：[模組名稱]  
**功能範圍**：
- [功能 1 描述]
- [功能 2 描述]
- [功能 3 描述]

**不包含**：
- [明確排除的功能]

### 2.2 技術環境

| 項目 | 規格 |
|------|------|
| 程式語言 | Java 21 / TypeScript 5.x / Python 3.12 |
| 框架 | Spring Boot 3.4.x / NestJS / FastAPI |
| 執行環境 | JVM 21 (GraalVM) / Node.js 22 LTS |
| 建置工具 | Gradle 8.x / npm / Poetry |
| 測試框架 | JUnit 5 + Mockito / Jest / pytest |
| 程式碼品質 | SonarQube / ESLint / Ruff |

### 2.3 相依套件

| 套件名稱 | 版本 | 用途 | 授權 |
|---------|------|------|------|
| spring-boot-starter-web | 3.4.x | Web 框架 | Apache 2.0 |
| spring-boot-starter-data-jpa | 3.4.x | ORM | Apache 2.0 |
| resilience4j | 2.x | 容錯處理 | Apache 2.0 |
| mapstruct | 1.6.x | DTO 轉換 | Apache 2.0 |
| lombok | 1.18.x | 程式碼簡化 | MIT |

---

## 3. 類別與函式設計（Class & Function Design）

### 3.1 類別圖（Class Diagram）

```
[使用 UML 類別圖或 Mermaid 呈現]

範例：

┌─────────────────────────────────────┐
│         <<interface>>               │
│         UserService                 │
├─────────────────────────────────────┤
│ + findById(id: Long): UserDTO       │
│ + create(req: CreateUserReq): UserDTO│
│ + update(id: Long, req): UserDTO    │
│ + delete(id: Long): void            │
│ + search(criteria): Page<UserDTO>   │
└──────────────┬──────────────────────┘
               │ implements
┌──────────────▼──────────────────────┐
│         UserServiceImpl             │
├─────────────────────────────────────┤
│ - userRepository: UserRepository    │
│ - passwordEncoder: PasswordEncoder  │
│ - eventPublisher: EventPublisher    │
├─────────────────────────────────────┤
│ + findById(id: Long): UserDTO       │
│ + create(req: CreateUserReq): UserDTO│
│ - validateEmail(email: String): void│
│ - publishEvent(event: DomainEvent)  │
└─────────────────────────────────────┘
```

### 3.2 類別詳細設計

#### 3.2.1 UserServiceImpl

| 屬性 | 描述 |
|------|------|
| **類別名稱** | `com.company.project.service.impl.UserServiceImpl` |
| **職責** | 使用者 CRUD 業務邏輯處理 |
| **設計模式** | Service Layer + Repository Pattern |
| **交易管理** | 寫入操作使用 `@Transactional` |
| **執行緒安全** | 無狀態設計，Spring Singleton 安全 |

**建構子**：
```java
/**
 * @param userRepository 使用者資料存取物件
 * @param passwordEncoder 密碼編碼器
 * @param eventPublisher 領域事件發布器
 */
public UserServiceImpl(
    UserRepository userRepository,
    PasswordEncoder passwordEncoder,
    ApplicationEventPublisher eventPublisher
)
```

### 3.3 方法規格

#### 方法：create（建立使用者）

| 項目 | 內容 |
|------|------|
| **方法簽名** | `public UserDTO create(CreateUserRequest request)` |
| **存取修飾** | public |
| **回傳型別** | `UserDTO` |
| **交易** | `@Transactional` |
| **冪等性** | 否（每次呼叫建立新使用者） |

**參數說明**：

| 參數名稱 | 型別 | 必填 | 驗證規則 | 說明 |
|---------|------|------|---------|------|
| request | CreateUserRequest | ✅ | @Valid | 建立使用者請求 |
| request.username | String | ✅ | 3-50 字元，英數底線 | 使用者帳號 |
| request.email | String | ✅ | RFC 5322 格式 | 電子郵件 |
| request.password | String | ✅ | ≥ 8 碼、含大小寫數字特殊字元 | 密碼 |

**處理流程**：

```
1. 驗證請求參數（Bean Validation）
2. 檢查 Email 是否已存在
   └─ 已存在 → 拋出 DuplicateEmailException
3. 檢查 Username 是否已存在
   └─ 已存在 → 拋出 DuplicateUsernameException
4. 密碼雜湊處理（bcrypt, cost=12）
5. 建立 User Entity 並設定預設值
   ├─ status = "PENDING_VERIFICATION"
   ├─ createdAt = now()
   └─ createdBy = currentUser
6. 儲存至資料庫
7. 發布 UserCreatedEvent 領域事件
8. 轉換為 UserDTO 並回傳
```

**虛擬碼（Pseudocode）**：

```java
@Transactional
public UserDTO create(CreateUserRequest request) {
    // Step 1: 參數驗證（由框架 @Valid 處理）

    // Step 2-3: 唯一性檢查
    if (userRepository.existsByEmail(request.getEmail())) {
        throw new DuplicateEmailException(request.getEmail());
    }
    if (userRepository.existsByUsername(request.getUsername())) {
        throw new DuplicateUsernameException(request.getUsername());
    }

    // Step 4: 密碼雜湊
    String encodedPassword = passwordEncoder.encode(request.getPassword());

    // Step 5: 建立實體
    User user = User.builder()
        .username(request.getUsername())
        .email(request.getEmail())
        .passwordHash(encodedPassword)
        .displayName(request.getDisplayName())
        .status(UserStatus.PENDING_VERIFICATION)
        .createdAt(Instant.now())
        .createdBy(SecurityUtils.getCurrentUser())
        .build();

    // Step 6: 儲存
    User saved = userRepository.save(user);

    // Step 7: 發布事件
    eventPublisher.publishEvent(new UserCreatedEvent(saved));

    // Step 8: 轉換回傳
    return UserMapper.INSTANCE.toDTO(saved);
}
```

**例外處理**：

| 例外類型 | 觸發條件 | HTTP 狀態碼 | 錯誤碼 |
|---------|---------|------------|--------|
| `ConstraintViolationException` | 參數驗證失敗 | 400 | E3001 |
| `DuplicateEmailException` | Email 已存在 | 409 | E2001 |
| `DuplicateUsernameException` | 帳號已存在 | 409 | E2002 |
| `DataAccessException` | 資料庫操作失敗 | 500 | E9001 |

---

## 4. 演算法邏輯（Algorithm Design）

### 4.1 演算法清單

| 演算法編號 | 名稱 | 用途 | 時間複雜度 | 空間複雜度 |
|-----------|------|------|-----------|-----------|
| ALG-001 | 密碼強度驗證 | 驗證密碼符合安全規則 | O(n) | O(1) |
| ALG-002 | Token 產生 | JWT Token 簽發 | O(1) | O(1) |
| ALG-003 | 分頁查詢 | 資料分頁與排序 | O(n log n) | O(n) |
| ALG-004 | 權限樹計算 | 角色權限繼承計算 | O(V+E) | O(V) |

### 4.2 演算法詳細描述

#### ALG-001：密碼強度驗證

**目的**：驗證使用者密碼符合企業安全政策

**輸入**：`password: String`  
**輸出**：`PasswordStrength { valid: boolean, score: int, issues: List<String> }`

**規則**：
| 規則 | 描述 | 分數 |
|------|------|------|
| 長度 ≥ 8 | 最低長度要求 | 必要 |
| 長度 ≥ 12 | 建議長度 | +1 |
| 含大寫字母 | A-Z 至少一個 | +1 |
| 含小寫字母 | a-z 至少一個 | +1 |
| 含數字 | 0-9 至少一個 | +1 |
| 含特殊字元 | !@#$%^&*等 | +1 |
| 不含常見密碼 | 比對常見密碼庫 | 必要 |
| 不含使用者資訊 | 不含帳號、Email | 必要 |

**虛擬碼**：

```
function validatePasswordStrength(password, userContext):
    issues = []
    score = 0

    // 必要規則
    if length(password) < 8:
        issues.add("密碼長度不足 8 碼")
        return { valid: false, score: 0, issues }

    if isCommonPassword(password):
        issues.add("密碼過於常見")
        return { valid: false, score: 0, issues }

    if containsUserInfo(password, userContext):
        issues.add("密碼不可包含個人資訊")
        return { valid: false, score: 0, issues }

    // 評分規則
    if length(password) >= 12: score += 1
    if hasUpperCase(password): score += 1 else issues.add("建議包含大寫字母")
    if hasLowerCase(password): score += 1 else issues.add("建議包含小寫字母")
    if hasDigit(password): score += 1 else issues.add("建議包含數字")
    if hasSpecialChar(password): score += 1 else issues.add("建議包含特殊字元")

    return { valid: score >= 3, score, issues }
```

---

## 5. 資料結構（Data Structures）

### 5.1 核心資料模型

#### User Entity

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true, length = 50)
    private String username;

    @Column(nullable = false, unique = true, length = 254)
    private String email;

    @Column(name = "password_hash", nullable = false, length = 256)
    private String passwordHash;

    @Column(name = "display_name", length = 100)
    private String displayName;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 30)
    private UserStatus status;

    @Column(name = "last_login_at")
    private Instant lastLoginAt;

    @Column(name = "failed_login_count", nullable = false)
    private int failedLoginCount = 0;

    @Column(name = "locked_until")
    private Instant lockedUntil;

    // 稽核欄位
    @Column(name = "created_at", nullable = false, updatable = false)
    private Instant createdAt;

    @Column(name = "created_by", nullable = false, updatable = false, length = 50)
    private String createdBy;

    @Column(name = "updated_at")
    private Instant updatedAt;

    @Column(name = "updated_by", length = 50)
    private String updatedBy;
}
```

#### UserStatus 列舉

```java
public enum UserStatus {
    PENDING_VERIFICATION,  // 待驗證
    ACTIVE,               // 啟用
    SUSPENDED,            // 停權
    LOCKED,               // 鎖定（登入失敗過多）
    DEACTIVATED           // 停用
}
```

### 5.2 DTO 定義

#### CreateUserRequest

```java
public record CreateUserRequest(
    @NotBlank @Size(min = 3, max = 50)
    @Pattern(regexp = "^[a-zA-Z0-9_]+$")
    String username,

    @NotBlank @Email @Size(max = 254)
    String email,

    @NotBlank @Size(min = 8, max = 128)
    String password,

    @Size(max = 100)
    String displayName
) {}
```

#### UserDTO

```java
public record UserDTO(
    Long id,
    String username,
    String email,
    String displayName,
    String status,
    Instant lastLoginAt,
    Instant createdAt
) {}
```

### 5.3 快取結構

| 快取 Key 模式 | Value 類型 | TTL | 用途 |
|-------------|-----------|-----|------|
| `user:{id}` | UserDTO JSON | 30 分鐘 | 使用者資料快取 |
| `user:email:{email}` | Long (userId) | 30 分鐘 | Email 反查 |
| `auth:token:{tokenId}` | TokenInfo JSON | 依 Token 效期 | Token 黑名單/白名單 |
| `auth:failcount:{userId}` | Integer | 30 分鐘 | 登入失敗計數 |

---

## 6. 錯誤處理機制（Error Handling）

### 6.1 例外階層設計

```
RuntimeException
└── BaseBusinessException (abstract)
    ├── ResourceNotFoundException
    │   ├── UserNotFoundException
    │   └── OrderNotFoundException
    ├── DuplicateResourceException
    │   ├── DuplicateEmailException
    │   └── DuplicateUsernameException
    ├── ValidationException
    │   └── PasswordPolicyException
    ├── AuthenticationException
    │   ├── InvalidCredentialsException
    │   └── AccountLockedException
    └── ExternalServiceException
        ├── SSOServiceException
        └── NotificationServiceException
```

### 6.2 全域例外處理器

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ApiResponse> handleNotFound(ResourceNotFoundException ex) {
        // HTTP 404, 錯誤碼依例外類型
    }

    @ExceptionHandler(DuplicateResourceException.class)
    public ResponseEntity<ApiResponse> handleDuplicate(DuplicateResourceException ex) {
        // HTTP 409, 錯誤碼依例外類型
    }

    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<ApiResponse> handleValidation(ConstraintViolationException ex) {
        // HTTP 400, 錯誤碼 E3001, 逐欄位列出驗證錯誤
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse> handleUnexpected(Exception ex) {
        // HTTP 500, 錯誤碼 E9001, 記錄完整堆疊
        // 不向客戶端暴露內部細節
    }
}
```

### 6.3 錯誤回應格式

```json
{
  "success": false,
  "code": "E2001",
  "message": "使用者可理解的錯誤訊息",
  "errors": [
    {
      "field": "email",
      "code": "DUPLICATE",
      "message": "此 Email 已被使用"
    }
  ],
  "timestamp": "2026-05-19T10:30:00Z",
  "traceId": "abc123-def456",
  "path": "/api/v1/users"
}
```

### 6.4 重試策略

| 場景 | 重試次數 | 間隔策略 | 逾時 |
|------|---------|---------|------|
| 資料庫暫態錯誤 | 3 次 | 指數退避（100ms, 200ms, 400ms） | 2 秒 |
| 外部 API 呼叫 | 3 次 | 指數退避（500ms, 1s, 2s） | 10 秒 |
| 訊息佇列發送 | 5 次 | 固定間隔（1 秒） | 30 秒 |
| 快取操作 | 1 次 | 立即重試 | 500ms |

---

## 7. 自動化測試規劃（Test Plan）

### 7.1 測試策略

```
                    ┌──────────┐
                   │  E2E Test │     ← 少量，關鍵流程
                  │  (Cypress)  │
                 ├──────────────┤
                │Integration Test│   ← 中量，API + DB
               │  (TestContainers) │
              ├────────────────────┤
             │     Unit Test        │ ← 大量，業務邏輯
            │   (JUnit 5 + Mockito)  │
           └──────────────────────────┘
                  測試金字塔
```

### 7.2 測試覆蓋率目標

| 測試類型 | 覆蓋率目標 | 範圍 |
|---------|-----------|------|
| 單元測試 | ≥ 80% 行覆蓋 | Service、Domain 層 |
| 整合測試 | 關鍵路徑 100% | Controller + Repository |
| E2E 測試 | 核心流程 100% | 使用者關鍵旅程 |

### 7.3 單元測試規格

#### 測試類別：UserServiceImplTest

| 測試案例 ID | 測試方法 | 測試場景 | 預期結果 |
|-----------|---------|---------|---------|
| UT-001 | test_create_success | 正常建立使用者 | 回傳 UserDTO，狀態為 PENDING |
| UT-002 | test_create_duplicateEmail | Email 已存在 | 拋出 DuplicateEmailException |
| UT-003 | test_create_duplicateUsername | 帳號已存在 | 拋出 DuplicateUsernameException |
| UT-004 | test_create_passwordEncoded | 密碼需雜湊 | passwordHash ≠ 原始密碼 |
| UT-005 | test_create_eventPublished | 建立成功後發布事件 | UserCreatedEvent 被發布 |
| UT-006 | test_findById_success | 查詢存在的使用者 | 回傳正確 UserDTO |
| UT-007 | test_findById_notFound | 查詢不存在的使用者 | 拋出 UserNotFoundException |

#### 測試範例

```java
@ExtendWith(MockitoExtension.class)
class UserServiceImplTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @Mock
    private ApplicationEventPublisher eventPublisher;

    @InjectMocks
    private UserServiceImpl userService;

    @Test
    @DisplayName("UT-001: 正常建立使用者 - 應回傳 UserDTO")
    void test_create_success() {
        // Given
        var request = new CreateUserRequest(
            "john_doe", "john@example.com", "P@ssw0rd123", "John"
        );
        when(userRepository.existsByEmail(anyString())).thenReturn(false);
        when(userRepository.existsByUsername(anyString())).thenReturn(false);
        when(passwordEncoder.encode(anyString())).thenReturn("hashed");
        when(userRepository.save(any(User.class))).thenAnswer(invocation -> {
            User user = invocation.getArgument(0);
            user.setId(1L);
            return user;
        });

        // When
        UserDTO result = userService.create(request);

        // Then
        assertNotNull(result);
        assertEquals("john_doe", result.username());
        assertEquals("PENDING_VERIFICATION", result.status());
        verify(eventPublisher).publishEvent(any(UserCreatedEvent.class));
    }

    @Test
    @DisplayName("UT-002: Email 已存在 - 應拋出 DuplicateEmailException")
    void test_create_duplicateEmail() {
        // Given
        var request = new CreateUserRequest(
            "john_doe", "existing@example.com", "P@ssw0rd123", "John"
        );
        when(userRepository.existsByEmail("existing@example.com")).thenReturn(true);

        // When & Then
        assertThrows(DuplicateEmailException.class, () -> userService.create(request));
        verify(userRepository, never()).save(any());
    }
}
```

### 7.4 整合測試規格

| 測試案例 ID | 測試場景 | 測試範圍 | 前置條件 |
|-----------|---------|---------|---------|
| IT-001 | POST /api/v1/users 建立使用者 | Controller → Service → DB | 空資料庫 |
| IT-002 | POST /api/v1/users 重複 Email | Controller → Service → DB | 已有同 Email 使用者 |
| IT-003 | GET /api/v1/users/{id} 查詢 | Controller → Service → DB → Cache | 資料庫有測試資料 |
| IT-004 | POST /api/v1/auth/login 登入 | Controller → Auth → DB | 已有驗證通過的使用者 |

### 7.5 效能測試規格

| 測試案例 | 工具 | 模擬條件 | 通過標準 |
|---------|------|---------|---------|
| 登入 API 壓力測試 | JMeter / k6 | 500 併發、持續 5 分鐘 | P95 < 200ms |
| 查詢 API 壓力測試 | JMeter / k6 | 1,000 併發、持續 10 分鐘 | P95 < 100ms |
| 建立使用者 API | JMeter / k6 | 100 併發、持續 5 分鐘 | P95 < 500ms |

---

## 8. 組態與環境設定

### 8.1 應用程式組態

| 組態項目 | 開發環境 | 測試環境 | 生產環境 | 說明 |
|---------|---------|---------|---------|------|
| server.port | 8080 | 8080 | 8080 | 服務埠號 |
| spring.datasource.url | localhost:5432 | sit-db:5432 | prd-db:5432 | 資料庫連線 |
| spring.redis.host | localhost | sit-redis | prd-redis | Redis 位址 |
| jwt.expiration | 3600 | 3600 | 1800 | Token 效期（秒） |
| logging.level.root | DEBUG | INFO | WARN | 日誌等級 |

### 8.2 敏感組態管理

| 組態項目 | 管理方式 | 存取控制 |
|---------|---------|---------|
| 資料庫密碼 | Kubernetes Secret / Vault | 僅維運團隊 |
| JWT 簽名金鑰 | Vault | 僅應用服務 |
| 第三方 API Key | Vault | 僅應用服務 |
| SSL 憑證 | Cert Manager | 自動管理 |

---

## 9. 建置與部署

### 9.1 建置指令

```bash
# 本地建置
./gradlew clean build

# 執行測試
./gradlew test

# 產生測試覆蓋率報告
./gradlew jacocoTestReport

# 建立 Docker Image
docker build -t project-name:latest .

# 靜態分析
./gradlew sonar
```

### 9.2 Dockerfile 規格

```dockerfile
# 多階段建置
FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app
COPY . .
RUN ./gradlew clean build -x test

FROM eclipse-temurin:21-jre-alpine
RUN addgroup -S app && adduser -S app -G app
USER app
WORKDIR /app
COPY --from=builder /app/build/libs/*.jar app.jar
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -q --spider http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### 9.3 健康檢查端點

| 端點 | 用途 | 回應 |
|------|------|------|
| /actuator/health | 存活探測（Liveness） | UP / DOWN |
| /actuator/health/readiness | 就緒探測（Readiness） | UP / DOWN |
| /actuator/info | 應用資訊 | 版本、建置時間 |
| /actuator/metrics | Prometheus 指標 | 指標資料 |

---

## 10. 程式碼品質標準

### 10.1 靜態分析規則

| 規則類型 | 工具 | 閾值 |
|---------|------|------|
| 程式碼重複 | SonarQube | < 3% |
| 認知複雜度 | SonarQube | 單一方法 < 15 |
| 技術債務 | SonarQube | < 2 小時 |
| 安全弱點 | SonarQube | 0 Critical, 0 Blocker |
| 測試覆蓋率 | JaCoCo | ≥ 80% |

### 10.2 Code Review 檢查要點

| 類別 | 檢查項目 |
|------|---------|
| 正確性 | 業務邏輯是否正確、邊界條件處理 |
| 安全性 | 輸入驗證、SQL 注入、XSS 防護 |
| 效能 | N+1 查詢、不必要的資料載入 |
| 可維護性 | 命名清晰、方法長度適當、註解充足 |
| 測試 | 測試覆蓋、測試案例品質 |

---

## 範例：訂單服務 TSD 摘要

### 核心方法
| 方法 | 輸入 | 輸出 | 複雜度 |
|------|------|------|--------|
| createOrder | CreateOrderRequest | OrderDTO | O(n)，n = 商品數 |
| cancelOrder | orderId, reason | void | O(1) |
| calculateTotal | List<OrderItem> | BigDecimal | O(n) |

### 測試案例數
| 測試類型 | 案例數 | 覆蓋率 |
|---------|--------|--------|
| 單元測試 | 45 | 87% |
| 整合測試 | 12 | 關鍵路徑 100% |
| 效能測試 | 3 | 核心 API |

---

> 📌 **填寫提醒**  
> 1. TSD 應由開發工程師撰寫，技術主管與架構師審查  
> 2. 虛擬碼應可直接轉換為實際程式碼  
> 3. 每個公開方法需有對應的單元測試案例  
> 4. 完成後需安排 Code Review 確認設計與實作一致  
> 5. 隨程式碼演進同步更新本文件
