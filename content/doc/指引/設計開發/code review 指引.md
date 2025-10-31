# Code Review 指引

## 目錄

1. [前言](#1-前言)
   - 1.1 [目的](#11-目的)
   - 1.2 [適用範圍](#12-適用範圍)
   - 1.3 [Code Review 的價值](#13-code-review-的價值)
2. [Code Review 基本原則](#2-code-review-基本原則)
   - 2.1 [核心原則](#21-核心原則)
   - 2.2 [責任分工](#22-責任分工)
3. [Code Review 流程](#3-code-review-流程)
   - 3.1 [提交 Pull Request (PR)](#31-提交-pull-request-pr)
   - 3.2 [指定 Reviewers](#32-指定-reviewers)
   - 3.3 [進行程式碼檢查](#33-進行程式碼檢查)
4. [詳細檢查項目](#4-詳細檢查項目)
   - 4.1 [程式碼風格與規範](#41-程式碼風格與規範)
   - 4.2 [邏輯正確性檢查](#42-邏輯正確性檢查)
   - 4.3 [效能考量檢查](#43-效能考量檢查)
   - 4.4 [安全性檢查](#44-安全性檢查)
   - 4.5 [測試覆蓋率檢查](#45-測試覆蓋率檢查)
5. [Code Review 工具與自動化](#5-code-review-工具與自動化)
   - 5.1 [GitHub Pull Request Review](#51-github-pull-request-review)
   - 5.2 [GitLab Merge Request Review](#52-gitlab-merge-request-review)
   - 5.3 [SonarQube 程式碼品質檢查](#53-sonarqube-程式碼品質檢查)
   - 5.4 [ESLint 與 Prettier（前端）](#54-eslint-與-prettier前端)
6. [實務操作指南](#6-實務操作指南)
   - 6.1 [Review 意見分類與標準](#61-review-意見分類與標準)
   - 6.2 [常見審查重點清單](#62-常見審查重點清單)
   - 6.3 [溝通技巧與最佳實務](#63-溝通技巧與最佳實務)
   - 6.4 [Review 會議與討論](#64-review-會議與討論)
7. [常見問題與解決方案](#7-常見問題與解決方案)
   - 7.1 [常見 Review 問題](#71-常見-review-問題)
   - 7.2 [效率提升技巧](#72-效率提升技巧)
8. [團隊協作與衝突處理](#8-團隊協作與衝突處理)
   - 8.1 [Review 意見衝突處理](#81-review-意見衝突處理)
   - 8.2 [跨團隊 Review 協作](#82-跨團隊-review-協作)
   - 8.3 [新人培訓與指導](#83-新人培訓與指導)
9. [特殊情況處理](#9-特殊情況處理)
   - 9.1 [緊急修正流程](#91-緊急修正流程)
   - 9.2 [大型重構 Review](#92-大型重構-review)
   - 9.3 [第三方程式碼整合](#93-第三方程式碼整合)
10. [持續改進與測量](#10-持續改進與測量)
    - 10.1 [Review 品質指標](#101-review-品質指標)
    - 10.2 [流程效率分析](#102-流程效率分析)
    - 10.3 [團隊成長追蹤](#103-團隊成長追蹤)
11. [參考資源與延伸閱讀](#11-參考資源與延伸閱讀)
    - 11.1 [程式碼品質標準](#111-程式碼品質標準)
    - 11.2 [安全性資源](#112-安全性資源)
    - 11.3 [工具文件](#113-工具文件)
    - 11.4 [最佳實務書籍](#114-最佳實務書籍)
12. [附錄](#12-附錄)
    - 12.1 [Review 檢查清單範本](#121-review-檢查清單範本)
    - 12.2 [團隊 Code Review 文化建立](#122-團隊-code-review-文化建立)

## 1. 前言

### 1.1 目的

本指引旨在建立標準化的程式碼審查流程，確保所有程式碼在合併至主分支前都經過充分的檢查與評審，以提升程式碼品質、降低潛在錯誤與技術負債，並促進團隊知識分享與技能提升。

### 1.2 適用範圍

- 所有提交至 Git 版本控制系統的程式碼
- 前端開發：Vue.js、TypeScript、Tailwind CSS
- 後端開發：Spring Boot、Java、Clean Architecture
- 資料庫相關：SQL、JPA、資料遷移腳本
- 配置檔案：Maven、Log4j2、應用程式設定檔

### 1.3 Code Review 的價值

- **提升程式碼品質**：及早發現錯誤、改善程式碼結構
- **知識分享**：促進團隊成員間的技術交流與學習
- **標準化**：確保程式碼風格一致性與最佳實務
- **風險控制**：降低生產環境問題發生機率
- **技能提升**：協助團隊成員持續成長

## 2. Code Review 基本原則

### 2.1 核心原則

- **建設性回饋**：提供具體、可行的改善建議
- **尊重與包容**：保持專業態度，專注於程式碼而非個人
- **及時回應**：在合理時間內完成審查（建議 24 小時內）
- **雙向學習**：Reviewer 和 Author 都應抱持學習心態
- **品質優先**：寧可多花時間審查，也不妥協程式碼品質

### 2.2 責任分工

- **Author（提交者）**：
  - 確保程式碼符合基本規範再提交
  - 撰寫清晰的 PR 描述
  - 積極回應 Reviewer 意見
  - 完成修改後重新請求審查

- **Reviewer（審查者）**：
  - 仔細檢查程式碼邏輯與品質
  - 提供建設性意見與改善建議
  - 驗證程式碼是否符合專案規範
  - 確認測試覆蓋率與文件完整性

## 3. Code Review 流程

### 3.1 提交 Pull Request (PR)

**步驟一：準備工作**

```bash
# 確保本地分支是最新的
git checkout main
git pull origin main

# 建立功能分支
git checkout -b feature/your-feature-name

# 開發完成後提交
git add .
git commit -m "feat: add new feature description"
git push origin feature/your-feature-name
```

**步驟二：建立 PR**

PR 標題格式：
```
[類型]: 簡短描述

範例：
feat: 新增使用者登入功能
fix: 修正資料庫連線逾時問題
refactor: 重構使用者服務層
docs: 更新 API 文件
```

**步驟三：撰寫 PR 描述範本**

```markdown
## 變更概述
簡述本次變更的目的與內容

## 變更類型
- [ ] 新功能 (feat)
- [ ] 錯誤修正 (fix)
- [ ] 重構 (refactor)
- [ ] 文件更新 (docs)
- [ ] 測試相關 (test)
- [ ] 建置相關 (build)

## 變更內容
- 新增了什麼功能
- 修正了什麼問題
- 重構了什麼部分

## 測試說明
- [ ] 單元測試已通過
- [ ] 整合測試已通過
- [ ] 手動測試已完成

## 檢查清單
- [ ] 程式碼符合專案規範
- [ ] 已新增或更新相關測試
- [ ] 已更新相關文件
- [ ] 無明顯效能問題
```

### 3.2 指定 Reviewers

**Reviewer 選擇原則：**

- **技術專長匹配**：選擇熟悉相關技術領域的同事
- **經驗層級平衡**：至少包含一位資深開發者
- **領域知識**：選擇了解業務邏輯的團隊成員
- **人數建議**：通常 2-3 位 Reviewer 較為適當

**自動指派規則（GitHub 範例）：**

```yaml
# .github/CODEOWNERS
# 全域預設
* @senior-dev @tech-lead

# 前端程式碼
/frontend/ @frontend-team @ux-designer

# 後端程式碼
/backend/ @backend-team @architect

# 資料庫相關
*.sql @dba @backend-lead

# 設定檔
*.yml *.yaml *.properties @devops @tech-lead
```

**自動指派規則（GitLab 範例）：**

```yaml
# .gitlab/CODEOWNERS
# 全域預設
* @senior-dev @tech-lead

# 前端程式碼
/frontend/ @frontend-team @ux-designer

# 後端程式碼
/backend/ @backend-team @architect

# 資料庫相關
*.sql @dba @backend-lead

# 設定檔
*.yml *.yaml *.properties @devops @tech-lead
```

**GitLab 自動化指派腳本：**

```bash
#!/bin/bash
# gitlab-auto-assign.sh - 根據變更檔案自動指派 Reviewer

PROJECT_ID="your-project-id"
MR_IID="$1"
GITLAB_TOKEN="your-access-token"
GITLAB_URL="https://gitlab.example.com"

# 取得 MR 變更的檔案
CHANGED_FILES=$(curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests/$MR_IID/changes" \
  | jq -r '.changes[].new_path')

ASSIGNEES=""

# 根據檔案類型決定指派對象
while IFS= read -r file; do
  case $file in
    *.java|*.kt)
      ASSIGNEES="$ASSIGNEES backend-lead"
      ;;
    *.vue|*.ts|*.js)
      ASSIGNEES="$ASSIGNEES frontend-lead"
      ;;
    *.sql|*/migration/*)
      ASSIGNEES="$ASSIGNEES dba"
      ;;
    *.yml|*.yaml|Dockerfile)
      ASSIGNEES="$ASSIGNEES devops-lead"
      ;;
  esac
done <<< "$CHANGED_FILES"

# 指派 Reviewers
for assignee in $(echo $ASSIGNEES | tr ' ' '\n' | sort -u); do
  curl --request PUT --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
    --header "Content-Type: application/json" \
    --data "{\"assignee_ids\": [$(get_user_id $assignee)]}" \
    "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests/$MR_IID"
done
```

### 3.3 進行程式碼檢查

**檢查層次：**

1. **自動化檢查（必須通過）**
   - CI/CD 建置成功
   - 自動化測試通過
   - 程式碼掃描無嚴重問題

2. **人工審查重點**
   - 業務邏輯正確性
   - 程式碼可讀性與維護性
   - 架構設計合理性
   - 安全性考量

## 4. 詳細檢查項目

### 4.1 程式碼風格與規範

**命名規範檢查：**

```java
// ✅ 良好範例
public class UserService {
    private static final int MAX_RETRY_COUNT = 3;
    private UserRepository userRepository;
    
    public Optional<User> findUserByEmail(String emailAddress) {
        // 實作內容
    }
}

// ❌ 不良範例
public class userservice {
    private static final int max = 3;
    private UserRepository ur;
    
    public Optional<User> finduser(String e) {
        // 實作內容
    }
}
```

**格式與排版檢查：**

- **縮排一致性**：使用 4 個空格（Java）或 2 個空格（TypeScript）
- **行長度限制**：建議不超過 120 字元
- **空行使用**：邏輯區塊間適當空行
- **括號位置**：遵循專案統一規範

```typescript
// ✅ TypeScript 良好範例
interface UserProfile {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
}

export class UserService {
  private readonly apiClient: ApiClient;

  constructor(apiClient: ApiClient) {
    this.apiClient = apiClient;
  }

  async getUserProfile(userId: string): Promise<UserProfile | null> {
    try {
      const response = await this.apiClient.get(`/users/${userId}`);
      return response.data;
    } catch (error) {
      console.error('Failed to fetch user profile:', error);
      return null;
    }
  }
}
```

### 4.2 邏輯正確性檢查

**邊界條件處理：**

```java
// ✅ 良好的邊界條件處理
public List<User> searchUsers(String keyword, int page, int size) {
    // 參數驗證
    if (keyword == null || keyword.trim().isEmpty()) {
        return Collections.emptyList();
    }
    
    if (page < 0) {
        page = 0;
    }
    
    if (size <= 0 || size > 100) {
        size = 20; // 預設值
    }
    
    return userRepository.findByKeyword(keyword, PageRequest.of(page, size));
}
```

**錯誤處理檢查：**

```java
// ✅ 適當的例外處理
@Service
public class PaymentService {
    
    public PaymentResult processPayment(PaymentRequest request) {
        try {
            validatePaymentRequest(request);
            return executePayment(request);
        } catch (InvalidPaymentException e) {
            log.warn("Invalid payment request: {}", e.getMessage());
            return PaymentResult.failure("INVALID_REQUEST", e.getMessage());
        } catch (PaymentGatewayException e) {
            log.error("Payment gateway error: {}", e.getMessage(), e);
            return PaymentResult.failure("GATEWAY_ERROR", "暫時無法處理付款，請稍後再試");
        } catch (Exception e) {
            log.error("Unexpected error during payment processing", e);
            return PaymentResult.failure("SYSTEM_ERROR", "系統錯誤，請聯繫客服");
        }
    }
}
```

### 4.3 效能考量檢查

**資料庫查詢優化：**

```java
// ❌ N+1 查詢問題
public List<OrderDto> getAllOrdersWithItems() {
    List<Order> orders = orderRepository.findAll();
    return orders.stream()
        .map(order -> {
            List<OrderItem> items = orderItemRepository.findByOrderId(order.getId()); // N+1 問題
            return new OrderDto(order, items);
        })
        .collect(Collectors.toList());
}

// ✅ 優化後的查詢
@Query("SELECT o FROM Order o LEFT JOIN FETCH o.orderItems")
public List<Order> findAllOrdersWithItems();

public List<OrderDto> getAllOrdersWithItems() {
    List<Order> orders = orderRepository.findAllOrdersWithItems();
    return orders.stream()
        .map(OrderDto::new)
        .collect(Collectors.toList());
}
```

**快取策略檢查：**

```java
// ✅ 適當的快取使用
@Service
public class ConfigurationService {
    
    @Cacheable(value = "system-config", key = "#configKey")
    public String getSystemConfig(String configKey) {
        return configRepository.findByKey(configKey)
            .map(Config::getValue)
            .orElse(null);
    }
    
    @CacheEvict(value = "system-config", key = "#configKey")
    public void updateSystemConfig(String configKey, String value) {
        configRepository.updateByKey(configKey, value);
    }
}
```

### 4.4 安全性檢查

**輸入驗證：**

```java
// ✅ 適當的輸入驗證
@RestController
public class UserController {
    
    @PostMapping("/users")
    public ResponseEntity<User> createUser(@Valid @RequestBody CreateUserRequest request) {
        // @Valid 註解會自動進行驗證
        return ResponseEntity.ok(userService.createUser(request));
    }
}

// DTO 中的驗證註解
public class CreateUserRequest {
    @NotBlank(message = "電子郵件不能為空")
    @Email(message = "電子郵件格式不正確")
    private String email;
    
    @NotBlank(message = "密碼不能為空")
    @Size(min = 8, max = 50, message = "密碼長度須在 8-50 字元之間")
    @Pattern(regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]",
             message = "密碼須包含大小寫字母、數字及特殊字元")
    private String password;
}
```

**SQL 注入防護：**

```java
// ✅ 使用參數化查詢
@Repository
public class UserRepository {
    
    @Query("SELECT u FROM User u WHERE u.email = :email AND u.status = :status")
    Optional<User> findByEmailAndStatus(@Param("email") String email, 
                                      @Param("status") UserStatus status);
}

// ❌ 避免字串拼接（容易 SQL 注入）
// String sql = "SELECT * FROM users WHERE email = '" + email + "'";
```

**敏感資訊處理：**

```java
// ✅ 密碼加密處理
@Service
public class AuthenticationService {
    
    private final PasswordEncoder passwordEncoder;
    
    public User registerUser(String email, String plainPassword) {
        String encodedPassword = passwordEncoder.encode(plainPassword);
        User user = new User(email, encodedPassword);
        return userRepository.save(user);
    }
    
    // 確保密碼不會出現在日誌中
    @Override
    public String toString() {
        return "User{id=" + id + ", email='" + email + "', password='[PROTECTED]'}";
    }
}
```

### 4.5 測試覆蓋率檢查

**單元測試要求：**

- **覆蓋率標準**：新增程式碼至少 80% 覆蓋率
- **測試類型**：單元測試、整合測試、端對端測試
- **測試命名**：清楚描述測試場景

```java
// ✅ 良好的測試範例
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    @DisplayName("當電子郵件存在時_應該返回使用者資料")
    void givenExistingEmail_whenFindByEmail_thenReturnUser() {
        // Given
        String email = "test@example.com";
        User expectedUser = new User(email, "encodedPassword");
        when(userRepository.findByEmail(email)).thenReturn(Optional.of(expectedUser));
        
        // When
        Optional<User> result = userService.findByEmail(email);
        
        // Then
        assertThat(result).isPresent();
        assertThat(result.get().getEmail()).isEqualTo(email);
        verify(userRepository).findByEmail(email);
    }
    
    @Test
    @DisplayName("當電子郵件不存在時_應該返回空的Optional")
    void givenNonExistingEmail_whenFindByEmail_thenReturnEmpty() {
        // Given
        String email = "nonexisting@example.com";
        when(userRepository.findByEmail(email)).thenReturn(Optional.empty());
        
        // When
        Optional<User> result = userService.findByEmail(email);
        
        // Then
        assertThat(result).isEmpty();
        verify(userRepository).findByEmail(email);
    }
}
```

**前端測試範例（TypeScript + Jest）：**

```typescript
// ✅ Vue 元件測試
import { mount } from '@vue/test-utils';
import UserProfile from '@/components/UserProfile.vue';

describe('UserProfile.vue', () => {
  it('should display user information correctly', () => {
    // Given
    const user = {
      id: '1',
      email: 'test@example.com',
      firstName: 'John',
      lastName: 'Doe'
    };
    
    // When
    const wrapper = mount(UserProfile, {
      props: { user }
    });
    
    // Then
    expect(wrapper.text()).toContain('John Doe');
    expect(wrapper.text()).toContain('test@example.com');
  });
  
  it('should emit edit event when edit button is clicked', async () => {
    // Given
    const user = { id: '1', email: 'test@example.com', firstName: 'John', lastName: 'Doe' };
    const wrapper = mount(UserProfile, { props: { user } });
    
    // When
    await wrapper.find('[data-testid="edit-button"]').trigger('click');
    
    // Then
    expect(wrapper.emitted('edit')).toBeTruthy();
    expect(wrapper.emitted('edit')?.[0]).toEqual([user.id]);
  });
});
```

## 5. Code Review 工具與自動化

### 5.1 GitHub Pull Request Review

**GitHub PR Review 工作流程：**

```yaml
# .github/workflows/pr-review.yml
name: PR Review Checks

on:
  pull_request:
    branches: [ main, develop ]

jobs:
  code-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up JDK 21
        uses: actions/setup-java@v3
        with:
          java-version: '21'
          distribution: 'temurin'
          
      - name: Cache Maven dependencies
        uses: actions/cache@v3
        with:
          path: ~/.m2
          key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
          
      - name: Run tests
        run: mvn clean test
        
      - name: Generate test report
        run: mvn jacoco:report
        
      - name: SonarQube Scan
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        run: mvn sonar:sonar
        
      - name: Comment PR
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '✅ 自動化檢查通過！請進行人工審查。'
            })
```

### 5.2 GitLab Merge Request Review

**GitLab MR Review 工作流程：**

```yaml
# .gitlab-ci.yml
stages:
  - test
  - code-quality
  - security

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"

cache:
  paths:
    - .m2/repository/

before_script:
  - apt-get update -y
  - apt-get install -y openjdk-21-jdk

unit-tests:
  stage: test
  script:
    - mvn clean test
    - mvn jacoco:report
  artifacts:
    reports:
      junit:
        - target/surefire-reports/TEST-*.xml
      coverage: target/site/jacoco/jacoco.xml
    paths:
      - target/site/jacoco/
  coverage: '/Total.*?([0-9]{1,3})%/'

code-quality:
  stage: code-quality
  script:
    - mvn sonar:sonar
      -Dsonar.projectKey=$CI_PROJECT_NAME
      -Dsonar.host.url=$SONAR_HOST_URL
      -Dsonar.login=$SONAR_TOKEN
  only:
    - merge_requests
    - main

security-scan:
  stage: security
  script:
    - mvn dependency-check:check
  artifacts:
    reports:
      dependency_scanning: target/dependency-check-report.json
  only:
    - merge_requests
```

**GitLab 自動化 Review 規則：**

```yaml
# .gitlab/merge_request_templates/Default.md
## Merge Request 檢查清單

### 變更說明
- [ ] 清楚描述變更內容與目的
- [ ] 標記相關的 Issue 編號

### 程式碼品質
- [ ] 程式碼遵循團隊規範
- [ ] 單元測試已通過
- [ ] 覆蓋率達到要求標準

### 安全性檢查
- [ ] 沒有硬編碼敏感資訊
- [ ] 輸入驗證完整
- [ ] 依賴項目無已知漏洞

### 效能考量
- [ ] 無明顯效能問題
- [ ] 資料庫查詢已優化
- [ ] 資源使用合理

### 文件更新
- [ ] API 文件已更新
- [ ] README 或相關文件已更新
- [ ] 變更日誌已記錄

/assign @tech-lead
/label ~"needs-review"
```

**GitLab Code Owners 設定：**

```yaml
# .gitlab/CODEOWNERS
# 全域規則
* @senior-developer @tech-lead

# Java 後端程式碼
*.java @backend-team
src/main/java/ @backend-team @architect

# 前端程式碼
src/main/resources/static/ @frontend-team
*.vue @frontend-team
*.ts @frontend-team

# 設定檔案
*.yml @devops-team
*.yaml @devops-team
*.properties @backend-team @devops-team

# 資料庫相關
*.sql @dba @backend-team
src/main/resources/db/ @dba @backend-team

# 文件
*.md @technical-writer @tech-lead
docs/ @technical-writer
```

**GitLab MR 自動化腳本：**

```bash
#!/bin/bash
# gitlab-mr-stats.sh - 收集 GitLab MR 統計資料

PROJECT_ID="your-project-id"
GITLAB_TOKEN="your-access-token"
GITLAB_URL="https://gitlab.example.com"

# 取得最近 30 天的 MR 資料
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests?state=merged&created_after=$(date -d '30 days ago' -I)" \
  | jq '.[] | {
      iid: .iid,
      title: .title,
      created_at: .created_at,
      merged_at: .merged_at,
      author: .author.name,
      reviewers: [.assignees[].name]
    }'

# 計算平均審查時間
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests?state=merged" \
  | jq -r '.[] | select(.merged_at != null) | 
    [.created_at, .merged_at] | @csv' \
  | while IFS=, read created merged; do
      created_ts=$(date -d "${created//\"/}" +%s)
      merged_ts=$(date -d "${merged//\"/}" +%s)
      hours=$(( (merged_ts - created_ts) / 3600 ))
      echo "MR 審查時間: $hours 小時"
    done
```

### 5.3 SonarQube 程式碼品質檢查

**SonarQube 設定檔範例：**

```properties
# sonar-project.properties
sonar.projectKey=java-tutorial
sonar.projectName=Java Tutorial
sonar.projectVersion=1.0

# 原始碼路徑
sonar.sources=src/main/java
sonar.tests=src/test/java

# 排除檔案
sonar.exclusions=**/target/**,**/node_modules/**

# Java 特定設定
sonar.java.coveragePlugin=jacoco
sonar.jacoco.reportPaths=target/jacoco.exec

# 品質閘門設定
sonar.qualitygate.wait=true
```

**SonarQube 規則重點：**

- **程式碼異味**：重複程式碼、過長方法、循環複雜度
- **錯誤**：潛在的 NullPointerException、資源洩漏
- **安全漏洞**：SQL 注入、XSS、敏感資訊暴露
- **覆蓋率**：單元測試覆蓋率要求

### 5.4 ESLint 與 Prettier（前端）

**ESLint 設定檔（.eslintrc.js）：**

```javascript
module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true
  },
  extends: [
    'eslint:recommended',
    '@typescript-eslint/recommended',
    '@vue/typescript/recommended',
    'prettier'
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module'
  },
  plugins: ['@typescript-eslint', 'vue'],
  rules: {
    // 程式碼品質規則
    'no-console': 'warn',
    'no-debugger': 'error',
    'no-unused-vars': 'error',
    
    // TypeScript 規則
    '@typescript-eslint/no-explicit-any': 'warn',
    '@typescript-eslint/no-unused-vars': 'error',
    
    // Vue 規則
    'vue/component-name-in-template-casing': ['error', 'PascalCase'],
    'vue/no-unused-components': 'error'
  }
};
```

**Prettier 設定檔（.prettierrc）：**

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
```

## 6. 實務操作指南

### 6.1 Review 意見分類與標準

**意見嚴重程度分級：**

| 級別 | 標籤 | 說明 | 範例 |
|------|------|------|------|
| 🔴 Must Fix | `must-fix` | 必須修正才能合併 | 安全漏洞、邏輯錯誤、建置失敗 |
| 🟡 Should Fix | `should-fix` | 強烈建議修正 | 效能問題、程式碼異味、測試不足 |
| 🔵 Consider | `consider` | 建議考慮改善 | 命名優化、程式碼重構建議 |
| 💬 Question | `question` | 詢問或討論 | 設計決策、實作方式討論 |
| 📝 Nitpick | `nitpick` | 小細節 | 格式問題、註解錯字 |

**Review 意見範例：**

```markdown
🔴 **Must Fix**: 潛在的 SQL 注入風險
這裡直接拼接 SQL 字串可能導致 SQL 注入攻擊，請使用參數化查詢。

建議修改：
```java
// 目前寫法（危險）
String sql = "SELECT * FROM users WHERE email = '" + email + "'";

// 建議寫法
@Query("SELECT u FROM User u WHERE u.email = :email")
Optional<User> findByEmail(@Param("email") String email);
```

🟡 **Should Fix**: 建議新增錯誤處理
這個方法沒有處理可能的例外情況，建議新增適當的錯誤處理機制。

🔵 **Consider**: 方法名稱可以更具描述性
`process()` 這個方法名稱不夠明確，建議改為 `processPaymentRequest()` 或類似的名稱。
```

### 6.2 常見審查重點清單

**後端程式碼檢查清單：**

```markdown
## Spring Boot 應用程式檢查清單

### 控制器層 (Controller)
- [ ] 是否有適當的輸入驗證（@Valid）
- [ ] HTTP 狀態碼是否正確使用
- [ ] 是否有適當的錯誤處理
- [ ] API 文件是否完整（Swagger 註解）
- [ ] 是否遵循 RESTful 設計原則

### 服務層 (Service)
- [ ] 商業邏輯是否正確實作
- [ ] 是否有適當的異常處理
- [ ] 交易邊界是否正確設定（@Transactional）
- [ ] 是否有適當的日誌記錄
- [ ] 方法職責是否單一且清楚

### 資料存取層 (Repository)
- [ ] 查詢效能是否優化
- [ ] 是否避免 N+1 查詢問題
- [ ] 索引策略是否合理
- [ ] 是否使用適當的快取策略

### 設定與安全
- [ ] 敏感資訊是否外部化設定
- [ ] 是否有適當的安全控制
- [ ] 日誌等級是否適當
- [ ] 資源是否正確釋放
```

**前端程式碼檢查清單：**

```markdown
## Vue.js 應用程式檢查清單

### 元件設計
- [ ] 元件職責是否單一
- [ ] Props 定義是否完整且有驗證
- [ ] 事件發射是否適當使用
- [ ] 元件名稱是否遵循 PascalCase

### 狀態管理
- [ ] 是否適當使用 Pinia/Vuex
- [ ] 狀態更新是否遵循不可變原則
- [ ] 非同步操作是否正確處理

### 效能考量
- [ ] 是否適當使用 v-memo 或 computed
- [ ] 列表渲染是否有適當的 key
- [ ] 是否避免不必要的重新渲染
- [ ] 圖片和資源是否優化

### 使用者體驗
- [ ] 載入狀態是否有適當指示
- [ ] 錯誤狀態是否有友善提示
- [ ] 響應式設計是否正確
- [ ] 無障礙設計是否考慮
```

### 6.3 溝通技巧與最佳實務

**提供建設性意見的技巧：**

```markdown
✅ 良好的 Review 意見範例：

"這個方法的邏輯看起來很複雜，建議考慮拆分成幾個小方法來提高可讀性。
例如可以將驗證邏輯、資料處理和結果回傳分別獨立出來。"

"這裡可能會有效能問題，因為在迴圈中進行資料庫查詢。
建議考慮使用批次查詢或 JOIN 來優化。"

❌ 應避免的 Review 意見範例：

"這段程式碼寫得很糟糕。"
"為什麼要這樣寫？"
"這樣不對。"
```

**回應 Review 意見的方式：**

```markdown
✅ 良好的回應範例：

"感謝建議！你說得對，我已經將方法拆分並新增了單元測試。
請再幫忙檢查一下。"

"關於效能問題，我採用了你建議的批次查詢方式。
測試結果顯示效能提升了約 60%。"

"這個設計選擇是因為 [具體原因]，但我同意你的觀點。
讓我重新考慮這個實作方式。"
```

### 6.4 Review 會議與討論

**何時需要同步討論：**

- 複雜的設計決策討論
- 多次往返仍未達成共識
- 涉及架構層面的重大變更
- 新技術或模式的引入

**Review 會議進行方式：**

1. **準備階段**（5 分鐘）
   - 簡述變更背景與目的
   - 說明主要變更內容

2. **逐段檢視**（15-20 分鐘）
   - 依序檢視重要程式碼片段
   - 針對 Review 意見進行討論
   - 現場釐清疑問

3. **總結與決議**（5 分鐘）
   - 確認需要修正的項目
   - 約定後續追蹤時間
   - 記錄重要決議

## 7. 常見問題與解決方案

### 7.1 常見 Review 問題

**問題一：Review 時間過長**

**原因：**
- PR 過大，包含太多變更
- 缺乏明確的檢查重點
- Reviewer 經驗不足

**解決方案：**
```markdown
1. 控制 PR 大小
   - 單次 PR 建議不超過 400 行程式碼
   - 將大功能拆分成多個小 PR
   - 使用 Draft PR 進行階段性審查

2. 建立 Review 檢查清單
   - 針對不同類型程式碼提供檢查要點
   - 使用自動化工具減少人工檢查負擔

3. 提升 Reviewer 技能
   - 定期舉辦 Code Review 培訓
   - 資深開發者帶領新手進行 Review
```

**問題二：Review 意見過於主觀**

**解決方案：**
```markdown
1. 建立客觀標準
   - 制定明確的程式碼規範
   - 使用工具自動檢查格式問題
   - 建立設計模式與最佳實務文件

2. 聚焦重要問題
   - 優先關注邏輯正確性與安全性
   - 避免過度糾結於個人喜好
   - 使用嚴重程度分級系統
```

**問題三：Review 品質不一致**

**解決方案：**
```markdown
1. 標準化流程
   - 使用統一的 Review 檢查清單
   - 建立 Review 範本與指引
   - 定期校準 Review 標準

2. 交叉驗證
   - 重要變更由多位 Reviewer 檢查
   - 定期回顧 Review 品質
   - 分享優秀的 Review 案例
```

### 7.2 效率提升技巧

**PR 準備階段優化：**

```bash
# 使用 pre-commit hook 自動檢查
# .git/hooks/pre-commit
#!/bin/sh
echo "執行程式碼品質檢查..."

# 執行測試
mvn test -q
if [ $? -ne 0 ]; then
    echo "❌ 測試失敗，請修正後再提交"
    exit 1
fi

# 執行程式碼格式檢查
mvn spotless:check -q
if [ $? -ne 0 ]; then
    echo "❌ 程式碼格式不符合規範，執行 mvn spotless:apply 修正"
    exit 1
fi

echo "✅ 所有檢查通過"
```

**Review 效率工具：**

```markdown
1. IDE 外掛程式
   - IntelliJ IDEA: CodeGlance Pro, Rainbow Brackets, GitLab Integration
   - VS Code: GitLens, Code Spell Checker, SonarLint, GitLab Workflow

2. 瀏覽器外掛
   - GitHub: Refined GitHub, Octotree
   - GitLab: GitLab Tree, GitLab MR Helper

3. 命令列工具
   - gh cli: GitHub 命令列工具
   - glab cli: GitLab 命令列工具
   - git-extras: 額外的 Git 命令
```

**GitLab CLI 常用指令：**

```bash
# 安裝 GitLab CLI
curl -s https://gitlab.com/gitlab-org/cli/-/releases/latest/downloads/glab | bash

# 設定認證
glab auth login

# 建立 MR
glab mr create --title "feat: add new feature" --description "Description of changes"

# 列出待審查的 MR
glab mr list --state opened --assignee @me

# 審查 MR
glab mr view 123
glab mr approve 123
glab mr merge 123

# 檢查 CI/CD 狀態
glab ci status

# 下載 MR 到本地進行測試
glab mr checkout 123
```

## 8. 團隊協作與衝突處理

### 8.1 Review 意見衝突處理

**意見分歧的常見情況：**

1. **技術實作方式分歧**
2. **程式碼風格偏好不同**
3. **效能 vs 可讀性的權衡**
4. **設計模式選擇差異**

**衝突解決機制：**

```markdown
## 衝突處理流程

### 第一階段：溝通討論
1. 雙方清楚說明各自觀點與理由
2. 提供具體程式碼範例或文件支持
3. 考慮不同角度的優缺點

### 第二階段：尋求共識
1. 找出雙方都能接受的替代方案
2. 參考團隊既有慣例與標準
3. 考慮專案現況與時程限制

### 第三階段：升級處理
1. 技術主管或架構師介入決策
2. 團隊會議討論達成共識
3. 建立新的團隊標準或指引
```

**建設性衝突解決範例：**

```markdown
# 情境：Array.forEach() vs for...of 迴圈

## Reviewer A 的觀點：
建議使用 for...of 迴圈，因為：
- 效能較好，避免函式呼叫開銷
- 可以使用 break/continue 控制流程
- 更直觀易懂

## Reviewer B 的觀點：
建議使用 Array.forEach()，因為：
- 函數式程式設計風格更現代
- 避免傳統迴圈的常見錯誤
- 與其他數組方法（map, filter）風格一致

## 達成共識：
依據使用情境決定：
- 簡單遍歷且不需中斷：使用 forEach()
- 需要 break/continue 或效能敏感：使用 for...of
- 建立團隊編碼指引明確規範
```

### 8.2 跨團隊 Review 協作

**跨團隊 Review 場景：**

- 前後端 API 介面變更
- 共用元件庫修改
- 微服務間介面調整
- 公共配置檔案變更

**協作流程建立：**

```yaml
# .github/CODEOWNERS 範例
# API 相關變更需要前後端團隊共同審查
/api/                    @backend-team @frontend-team
/shared/                 @backend-team @frontend-team

# 基礎設施變更需要 DevOps 團隊審查
*.yml                    @devops-team
*.yaml                   @devops-team
/infrastructure/         @devops-team

# 安全相關變更需要安全團隊審查
/security/               @security-team @backend-team
**/auth/**               @security-team @backend-team
```

```yaml
# .gitlab/CODEOWNERS 範例
# API 相關變更需要前後端團隊共同審查
/api/                    @backend-team @frontend-team
/shared/                 @backend-team @frontend-team

# 基礎設施變更需要 DevOps 團隊審查
*.yml                    @devops-team
*.yaml                   @devops-team
/infrastructure/         @devops-team

# 安全相關變更需要安全團隊審查
/security/               @security-team @backend-team
**/auth/**               @security-team @backend-team

# GitLab 特有功能：可設定必須審查者數量
^[Backend Team] @backend-group (2)
^[DevOps Team] @devops-group (1)
```

**跨團隊 Review 最佳實務：**

```markdown
## 跨團隊 Review 指引

### 1. 提前溝通
- 重大變更前先與相關團隊討論
- 建立變更影響評估機制
- 設定合理的 Review 時間期待

### 2. 清楚的變更說明
- 詳細說明變更原因與影響範圍
- 提供測試方法與驗證步驟
- 附上相關文件或設計圖

### 3. 專業領域分工
- 各團隊專注於自己的專業領域
- 避免越界指導非專業領域
- 尊重其他團隊的技術決策

### 4. 建立溝通橋樑
- 指定跨團隊聯絡人
- 定期舉辦技術交流會議
- 建立共同的技術決策流程
```

### 8.3 新人培訓與指導

**新人 Code Review 培訓計畫：**

```markdown
## 新人 Code Review 培訓階段

### 第一階段：觀察學習（1-2週）
**目標：** 了解團隊 Review 風格與標準

**活動：**
- 觀察資深同事的 Review 過程
- 閱讀歷史 PR 與 Review 意見
- 學習團隊編碼規範與工具使用

**材料：**
- 團隊 Code Review 指引
- 過去 3 個月的優秀 Review 案例
- 專案技術文件與架構說明

### 第二階段：協助審查（2-3週）
**目標：** 開始參與 Review，但有資深同事指導

**活動：**
- 與資深同事一起 Review 簡單的 PR
- 學習如何提出建設性意見
- 練習使用 Review 工具與流程

**指導重點：**
- 如何識別常見問題
- 怎樣給出友善且有建設性的回饋
- Review 意見的優先順序判斷

### 第三階段：獨立審查（3-4週）
**目標：** 獨立進行簡單 PR 的 Review

**活動：**
- 獨立 Review 新功能與錯誤修正
- 定期與 mentor 討論 Review 心得
- 參與團隊 Review 標準討論

**成長指標：**
- 能識別基本的程式碼問題
- Review 意見獲得正面回饋
- 與其他開發者良好協作
```

**Mentor 指導技巧：**

```markdown
## Mentor 指導新人 Review 技巧

### 1. 循序漸進
- 從簡單的格式問題開始
- 逐步引導到邏輯與架構層面
- 避免一次給予過多資訊

### 2. 示範與解釋
- 展示優秀的 Review 範例
- 解釋背後的思考邏輯
- 分享個人經驗與教訓

### 3. 鼓勵與糾正
- 正面肯定新人的進步
- 溫和指出改善空間
- 提供具體的改善建議

### 4. 營造學習環境
- 鼓勵提問與討論
- 分享相關學習資源
- 建立互相學習的氛圍
```

## 9. 特殊情況處理

### 9.1 緊急修正流程

**緊急修正定義：**

- 生產環境嚴重錯誤（P0/P1）
- 安全漏洞需立即修補
- 服務中斷需緊急恢復

**緊急修正 Review 流程：**

```markdown
## 緊急修正 Review 程序

### 1. 緊急修正分類
**P0 - 立即修正（4小時內）**
- 系統完全無法使用
- 資料遺失或損毀
- 嚴重安全漏洞

**P1 - 緊急修正（24小時內）**
- 核心功能無法使用
- 效能嚴重下降
- 影響大量使用者

### 2. 簡化 Review 流程
- 減少 Reviewer 數量（1-2位資深開發者）
- 聚焦於修正邏輯正確性
- 可暫時略過非關鍵檢查項目

### 3. 後續補強措施
- 修正後進行完整的 Review
- 分析問題根本原因
- 建立預防措施與監控
```

**緊急修正 PR 範本：**

```markdown
## 🚨 緊急修正 PR

### 問題描述
- **嚴重程度：** P0/P1
- **影響範圍：** [描述受影響的功能或使用者]
- **問題現象：** [具體描述問題]

### 修正內容
- **修正方式：** [簡述修正邏輯]
- **測試驗證：** [說明如何驗證修正有效]
- **風險評估：** [評估修正可能帶來的風險]

### 後續計畫
- [ ] 進行完整測試
- [ ] 補充完整文件
- [ ] 分析根本原因
- [ ] 建立預防措施

**緊急聯絡人：** @tech-lead @on-call-engineer
```

### 9.2 大型重構 Review

**大型重構 Review 策略：**

```markdown
## 大型重構 Review 方法

### 1. 分階段 Review
**階段一：設計審查**
- 重構計畫與設計文件審查
- 架構變更合理性評估
- 風險分析與緩解措施

**階段二：分批實作審查**
- 將重構分成多個小 PR
- 每個 PR 專注於特定範圍
- 保持每次變更的可理解性

**階段三：整合測試審查**
- 整體功能完整性驗證
- 效能影響評估
- 相容性確認

### 2. Review 重點調整
- 著重架構層面的合理性
- 關注向後相容性
- 評估遷移策略完整性
- 確認回滾機制可行性
```

**重構 PR 組織範例：**

```markdown
# 使用者服務重構系列 PR

## PR 1/5: 抽取使用者介面定義
- 定義 UserService 介面
- 抽取共用的資料傳輸物件
- 不影響現有功能

## PR 2/5: 實作新的使用者服務
- 實作 UserServiceImpl
- 新增對應的單元測試
- 並行存在，不影響現有服務

## PR 3/5: 逐步遷移控制器
- 修改 UserController 使用新服務
- 段階性切換，保持功能完整
- 新增整合測試驗證

## PR 4/5: 清理舊有實作
- 移除舊的服務實作
- 清理不再使用的程式碼
- 更新相關文件

## PR 5/5: 效能優化與最終調整
- 根據使用情況進行效能調整
- 完善日誌與監控
- 更新部署腳本
```

### 9.3 第三方程式碼整合

**第三方程式碼 Review 重點：**

```markdown
## 第三方程式碼整合檢查

### 1. 授權與合規檢查
- [ ] 檢查程式庫授權相容性
- [ ] 確認商業使用限制
- [ ] 評估長期維護風險

### 2. 安全性評估
- [ ] 檢查已知安全漏洞
- [ ] 評估程式庫信譽度
- [ ] 審查權限需求

### 3. 技術相容性
- [ ] 版本相容性確認
- [ ] 效能影響評估
- [ ] 與現有架構整合度

### 4. 維護性考量
- [ ] 程式庫活躍度評估
- [ ] 文件完整性確認
- [ ] 社群支援程度
```

**依賴管理 Review 範例：**

```xml
<!-- Maven 依賴審查範例 -->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.12.0</version>
    <!-- ✅ 審查要點：
    1. 版本是否為最新穩定版
    2. 是否有已知安全漏洞
    3. 授權是否符合專案需求（Apache 2.0）
    4. 是否與現有依賴衝突
    -->
</dependency>
```

## 10. 持續改進與測量

### 10.1 Review 品質指標

**量化指標：**

```markdown
## Code Review 關鍵指標 (KPI)

### 效率指標
- **Review 平均時間：** PR 建立到核准的時間
- **回合數：** 平均需要幾輪修正才核准
- **等待時間：** Author 等待 Review 的平均時間

### 品質指標
- **缺陷發現率：** Review 階段發現的問題數量
- **生產錯誤率：** 通過 Review 後仍出現的問題
- **測試覆蓋率：** 程式碼測試覆蓋程度

### 參與度指標
- **Review 參與率：** 團隊成員參與 Review 的比例
- **意見回應率：** Review 意見的回應與處理率
- **知識分享程度：** 透過 Review 學習到的新知識
```

**指標收集與分析：**

```bash
# GitHub API 腳本範例：收集 Review 數據
#!/bin/bash
# 取得最近 30 天的 PR 統計
gh pr list --state merged --limit 100 --json number,title,createdAt,mergedAt,reviews

# 分析 Review 時間
gh pr view $PR_NUMBER --json reviews,createdAt,mergedAt \
  | jq '.reviews | length' # Review 數量

# 計算平均 Review 時間
gh pr list --state merged --limit 50 --json createdAt,mergedAt \
  | jq -r '.[] | [.createdAt, .mergedAt] | @csv' \
  | while IFS=, read created merged; do
      # 計算時間差並統計
    done
```

```bash
# GitLab API 腳本範例：收集 Review 數據
#!/bin/bash
PROJECT_ID="your-project-id"
GITLAB_TOKEN="your-access-token"
GITLAB_URL="https://gitlab.example.com"

# 取得最近 30 天的 MR 統計
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests?state=merged&created_after=$(date -d '30 days ago' -I)" \
  | jq '.[] | {
      iid: .iid,
      title: .title,
      created_at: .created_at,
      merged_at: .merged_at,
      author: .author.name,
      reviewers: [.assignees[].name]
    }'

# 分析 MR Review 數據
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests/$MR_IID/notes" \
  | jq '[.[] | select(.system == false)] | length' # 評論數量

# 計算平均 Review 時間
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests?state=merged" \
  | jq -r '.[] | select(.merged_at != null) | 
    [.created_at, .merged_at] | @csv' \
  | while IFS=, read created merged; do
      created_ts=$(date -d "${created//\"/}" +%s)
      merged_ts=$(date -d "${merged//\"/}" +%s)
      hours=$(( (merged_ts - created_ts) / 3600 ))
      echo "MR 審查時間: $hours 小時"
    done

# GitLab CI/CD 成功率統計
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "$GITLAB_URL/api/v4/projects/$PROJECT_ID/pipelines?per_page=100" \
  | jq -r '.[] | [.status, .created_at] | @csv' \
  | awk -F, '{status[$1]++} END {for (s in status) print s": "status[s]}'
```

### 10.2 流程效率分析

**瓶頸識別與改善：**

```markdown
## Review 流程瓶頸分析

### 常見瓶頸點
1. **Reviewer 回應時間過長**
   - 原因：工作負荷過重、優先順序不明確
   - 改善：設定 SLA、自動提醒機制

2. **Review 品質不一致**
   - 原因：標準不明確、經驗差異大
   - 改善：標準化檢查清單、培訓制度

3. **大型 PR 難以審查**
   - 原因：變更範圍過大、上下文複雜
   - 改善：拆分 PR、提供設計文件

### 改善措施
```

**自動化改善範例：**

```yaml
# GitHub Actions: 自動化 Review 提醒
name: Review Reminder
on:
  schedule:
    - cron: '0 9 * * 1-5'  # 每個工作日早上 9 點

jobs:
  remind-reviewers:
    runs-on: ubuntu-latest
    steps:
      - name: Check pending PRs
        uses: actions/github-script@v6
        with:
          script: |
            const { data: prs } = await github.rest.pulls.list({
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'open'
            });
            
            for (const pr of prs) {
              const createdDays = Math.floor(
                (Date.now() - new Date(pr.created_at)) / (1000 * 60 * 60 * 24)
              );
              
              if (createdDays > 2) {
                github.rest.issues.createComment({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pr.number,
                  body: `🔔 此 PR 已等待審查 ${createdDays} 天，請相關 reviewers 協助審查。`
                });
              }
            }
```

```yaml
# GitLab CI: 自動化 Review 提醒
stages:
  - schedule

review-reminder:
  stage: schedule
  image: alpine:latest
  before_script:
    - apk add --no-cache curl jq
  script:
    - |
      PROJECT_ID="${CI_PROJECT_ID}"
      GITLAB_TOKEN="${GITLAB_ACCESS_TOKEN}"
      GITLAB_URL="${CI_SERVER_URL}"
      
      # 取得所有開啟的 MR
      MRS=$(curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
        "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests?state=opened")
      
      echo "$MRS" | jq -r '.[] | select(.created_at < (now - 2*24*3600 | strftime("%Y-%m-%dT%H:%M:%S.%fZ"))) | 
        "MR !\(.iid) 已等待審查超過 2 天，標題：\(.title)，作者：\(.author.name)"'
      
      # 對超過 2 天的 MR 添加提醒評論
      echo "$MRS" | jq -r '.[] | select(.created_at < (now - 2*24*3600 | strftime("%Y-%m-%dT%H:%M:%S.%fZ"))) | .iid' | \
      while read mr_iid; do
        curl --request POST --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
          --header "Content-Type: application/json" \
          --data "{\"body\": \"🔔 此 MR 已等待審查超過 2 天，請相關 reviewers 協助審查。\"}" \
          "$GITLAB_URL/api/v4/projects/$PROJECT_ID/merge_requests/$mr_iid/notes"
      done
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
  # 需要在 GitLab 中設定 schedule pipeline，每日執行
```

### 10.3 團隊成長追蹤

**個人成長指標：**

```markdown
## 開發者 Review 成長追蹤

### 技能發展指標
- **Review 深度：** 從格式問題到架構建議的進展
- **問題識別能力：** 發現潛在問題的準確性
- **溝通技巧：** Review 意見的建設性與友善度

### 知識擴展指標
- **技術廣度：** 能審查的技術領域範圍
- **最佳實務：** 對業界標準的了解程度
- **領域知識：** 對專案業務邏輯的理解

### 協作能力指標
- **團隊貢獻：** 協助他人成長的程度
- **衝突處理：** 建設性解決技術分歧
- **知識分享：** 主動分享經驗與學習心得
```

**成長追蹤工具：**

```markdown
## 個人 Review 成長記錄表

### 月度自評（每月填寫）
| 項目 | 上月評分 | 本月評分 | 改善行動 |
|------|----------|----------|----------|
| 問題識別能力 | 3/5 | 4/5 | 學習安全最佳實務 |
| 溝通技巧 | 4/5 | 4/5 | 參加溝通技巧工作坊 |
| 技術廣度 | 3/5 | 3/5 | 學習前端框架 |

### 季度目標設定
- **技能目標：** 能夠審查前端 Vue.js 程式碼
- **貢獻目標：** 指導 1-2 位新進同事
- **學習目標：** 完成微服務架構課程

### 年度成長回顧
- **主要成就：** 成為團隊 Review 標準制定者
- **學習收穫：** 掌握 Spring Boot 最佳實務
- **明年規劃：** 發展為技術 Mentor 角色
```

## 11. 參考資源與延伸閱讀

### 11.1 程式碼品質標準

**Java 開發規範：**
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- [Oracle Java Code Conventions](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html)
- [Spring Boot Best Practices](https://spring.io/guides)

**JavaScript/TypeScript 規範：**
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html)
- [Vue.js Style Guide](https://vuejs.org/style-guide/)

### 11.2 安全性資源

**OWASP 安全指引：**

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)

### 11.3 工具文件

**靜態程式碼分析：**

- [SonarQube Documentation](https://docs.sonarqube.org/)
- [Checkstyle](https://checkstyle.sourceforge.io/)
- [PMD](https://pmd.github.io/)
- [SpotBugs](https://spotbugs.github.io/)

**版本控制與 CI/CD：**

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [GitLab Merge Requests](https://docs.gitlab.com/ee/user/project/merge_requests/)
- [GitLab Code Review](https://docs.gitlab.com/ee/development/code_review.html)
- [Conventional Commits](https://www.conventionalcommits.org/)

### 11.4 最佳實務書籍

**程式碼品質：**

- 《Clean Code》by Robert C. Martin
- 《Effective Java》by Joshua Bloch
- 《Refactoring》by Martin Fowler
- 《Code Complete》by Steve McConnell

**Code Review：**

- 《Best Kept Secrets of Peer Code Review》by Jason Cohen
- 《The Pragmatic Programmer》by David Thomas & Andrew Hunt

## 12. 附錄

### 12.1 Review 檢查清單範本

```markdown
## Code Review 檢查清單

### 基本要求
- [ ] 建置成功，無編譯錯誤
- [ ] 所有測試通過
- [ ] 程式碼覆蓋率達標（≥80%）
- [ ] 無嚴重的靜態分析警告

### 程式碼品質
- [ ] 方法長度適中（建議 ≤30 行）
- [ ] 類別職責單一且清楚
- [ ] 變數和方法命名有意義
- [ ] 沒有重複程式碼

### 邏輯正確性
- [ ] 業務邏輯實作正確
- [ ] 邊界條件處理適當
- [ ] 錯誤處理完整
- [ ] 並行安全考量

### 效能與安全
- [ ] 沒有明顯效能問題
- [ ] 資料庫查詢已優化
- [ ] 輸入驗證充分
- [ ] 敏感資訊處理安全

### 文件與測試
- [ ] 程式碼註解充分且準確
- [ ] API 文件完整
- [ ] 測試案例涵蓋主要場景
- [ ] 測試資料獨立且可重複
```

### 12.2 團隊 Code Review 文化建立

**推動策略：**

1. **由上而下支持**
   - 管理層明確支持 Code Review 制度
   - 將 Code Review 納入開發流程
   - 提供必要的時間與資源

2. **漸進式導入**
   - 從核心模組開始實施
   - 逐步擴展到整個專案
   - 持續調整流程與標準

3. **持續改善**
   - 定期回顧 Review 效果
   - 收集團隊回饋並調整
   - 分享成功案例與經驗

### 12.3 Code Review 常用英文術語

**基本術語：**

| 英文 | 中文 | 說明 |
|------|------|------|
| Pull Request (PR) | 拉取請求 | GitHub 提交程式碼變更的請求 |
| Merge Request (MR) | 合併請求 | GitLab 提交程式碼變更的請求 |
| Code Review | 程式碼審查 | 檢查程式碼品質的過程 |
| Reviewer | 審查者 | 負責檢查程式碼的人員 |
| Author | 作者 | 提交程式碼的開發者 |
| Merge | 合併 | 將變更整合到主分支 |
| Approve | 核准 | 同意合併程式碼變更 |
| Request Changes | 要求修改 | 需要修正後才能合併 |
| LGTM | Looks Good To Me | 看起來不錯，可以合併 |
| WIP | Work In Progress | 進行中的工作 |
| RFC | Request For Comments | 徵求意見 |
| Draft | 草稿 | 尚未準備好審查的 PR/MR |
| Squash | 壓縮 | 將多個 commit 合併為一個 |
| Rebase | 變基 | 重新設定 commit 的基底 |

**Review 意見常用語：**

```markdown
## 建議與修正
- "Consider using..." (考慮使用...)
- "This could be improved by..." (這可以透過...來改善)
- "What do you think about..." (你覺得...如何)
- "This might cause..." (這可能會導致...)

## 問題指出
- "This appears to be..." (這似乎是...)
- "I'm concerned about..." (我擔心...)
- "This could lead to..." (這可能導致...)
- "There's a potential issue with..." (這裡可能有問題...)

## 正面回饋
- "Nice implementation!" (很好的實作！)
- "Good catch!" (發現得好！)
- "This is much cleaner." (這樣更簡潔。)
- "Great refactoring!" (很棒的重構！)
```

### 12.4 快速參考卡

**Review 前檢查清單：**

```markdown
## 提交前自我檢查 ✅

### 基本檢查
- [ ] 程式碼可以正常編譯
- [ ] 所有測試通過
- [ ] 符合團隊編碼規範
- [ ] 移除 debug 程式碼和 console.log

### 功能檢查
- [ ] 實作符合需求規格
- [ ] 邊界條件已處理
- [ ] 錯誤處理完整
- [ ] 效能考量適當

### 文件檢查
- [ ] 新增必要的程式碼註解
- [ ] 更新相關 API 文件
- [ ] 補充或更新 README
- [ ] 新增測試案例說明
```

```markdown
## GitLab MR 提交前檢查 ✅

### GitLab 特有檢查
- [ ] MR 標題清楚描述變更內容
- [ ] 已連結相關的 Issue
- [ ] 設定適當的 Labels 和 Milestone
- [ ] 指派合適的 Reviewers 和 Assignees
- [ ] CI/CD Pipeline 執行成功
- [ ] 安全掃描通過（如有設定）

### GitLab CI/CD 檢查
- [ ] .gitlab-ci.yml 語法正確
- [ ] Docker 映像檔可正常建置
- [ ] 測試階段全部通過
- [ ] 程式碼品質檢查通過
- [ ] 部署腳本可正常執行

### GitLab 協作檢查
- [ ] 已通知相關團隊成員
- [ ] 設定合適的合併策略
- [ ] 確認分支保護規則
- [ ] 檢查合併衝突
```

**常見問題快速修正：**

```java
// ❌ 常見問題：未處理 null 值
public String getUserName(User user) {
    return user.getName().toUpperCase();
}

// ✅ 修正：新增 null 檢查
public String getUserName(User user) {
    if (user == null || user.getName() == null) {
        return "UNKNOWN";
    }
    return user.getName().toUpperCase();
}

// ❌ 常見問題：資源未關閉
public String readFile(String path) throws IOException {
    FileReader reader = new FileReader(path);
    // ... 處理檔案
    return content;
}

// ✅ 修正：使用 try-with-resources
public String readFile(String path) throws IOException {
    try (FileReader reader = new FileReader(path);
         BufferedReader buffered = new BufferedReader(reader)) {
        // ... 處理檔案
        return content;
    }
}
```

### 12.5 工具設定範例

**VS Code 設定檔案（.vscode/settings.json）：**

```json
{
  "java.format.settings.url": "https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-java-google-style.xml",
  "java.checkstyle.configuration": "${workspaceFolder}/checkstyle.xml",
  "java.test.config": {
    "workingDirectory": "${workspaceFolder}"
  },
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true,
    "source.fixAll": true
  },
  "files.exclude": {
    "**/target": true,
    "**/.classpath": true,
    "**/.project": true,
    "**/.settings": true
  }
}
```

**IntelliJ IDEA 程式碼範本：**

```xml
<!-- Live Template: review-comment -->
<template name="review" value="// TODO: Review - $COMMENT$&#10;// @reviewer: $REVIEWER$&#10;// @date: $DATE$" description="Add review comment">
  <variable name="COMMENT" expression="" defaultValue="&quot;Add your review comment here&quot;" alwaysStopAt="true" />
  <variable name="REVIEWER" expression="user()" defaultValue="" alwaysStopAt="true" />
  <variable name="DATE" expression="date(&quot;yyyy-MM-dd&quot;)" defaultValue="" alwaysStopAt="false" />
  <context>
    <option name="JAVA_CODE" value="true" />
  </context>
</template>
```

---

**文件版本：** v2.0  
**最後更新：** 2025年8月29日  
**維護者：** 開發團隊  
**審核者：** 技術主管

**變更記錄：**

- v1.0 (2025-08-20): 初版建立
- v2.0 (2025-08-29): 新增團隊協作、特殊情況處理、持續改進等章節
