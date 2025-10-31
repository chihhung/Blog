以下是完整的 **《JdbcTemplate 安全 SQL 實作指引文件》Markdown 版本**，可直接放入你的 Git Repository（例如 `/docs/security/jdbctemplate-sql-guideline.md`），作為團隊安全規範或 Code Review checklist 使用。

---

````markdown
# 🧭 JdbcTemplate 安全 SQL 實作指引文件
**版本：v1.0**  
**適用範圍：** Spring Boot 專案中使用 `JdbcTemplate` 或 `NamedParameterJdbcTemplate` 的資料存取層  
**目的：** 防止 SQL Injection 攻擊與弱掃誤判  

---

## 1️⃣ 目的與原則

SQL Injection（SQL 注入）是 OWASP Top 10 的主要風險之一。  
若在 API 中直接拼接 SQL 字串（尤其包含前端輸入），將導致弱掃報告出現 Injection 問題，甚至被惡意利用。

**安全實作原則：**
1. 所有 SQL 查詢必須採用 **參數化查詢（Parameterized Query）**。  
2. 不可直接拼接使用者輸入字串到 SQL。  
3. 動態欄位或排序需求必須使用 **白名單機制（Whitelist）**。  
4. 禁止讓 client 直接傳入完整 SQL。  
5. 所有 DB 帳號採用最小權限原則（Least Privilege）。

---

## 2️⃣ 正確安全作法範例

### ✅ 查詢範例
```java
String sql = "SELECT id, name, email FROM users WHERE email = ?";
return jdbcTemplate.query(sql, new Object[]{email}, new UserRowMapper());
````

---

### ✅ 插入範例

```java
String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
jdbcTemplate.update(sql, name, email);
```

---

### ✅ 更新範例

```java
String sql = "UPDATE users SET status = ? WHERE id = ?";
jdbcTemplate.update(sql, status, id);
```

---

### ✅ 刪除範例

```java
String sql = "DELETE FROM users WHERE id = ?";
jdbcTemplate.update(sql, id);
```

---

### ✅ 動態查詢（條件可變）

> 重點：條件以程式判斷拼接，但參數仍使用 `?` 綁定。

```java
StringBuilder sql = new StringBuilder("SELECT * FROM users WHERE 1=1");
List<Object> params = new ArrayList<>();

if (name != null && !name.isEmpty()) {
    sql.append(" AND name LIKE ?");
    params.add("%" + name + "%");
}

if (status != null && !status.isEmpty()) {
    sql.append(" AND status = ?");
    params.add(status);
}

return jdbcTemplate.query(sql.toString(), params.toArray(), new UserRowMapper());
```

---

### ✅ 排序欄位安全（白名單）

```java
List<String> allowedSortFields = List.of("name", "email", "created_at");
String sortColumn = allowedSortFields.contains(sortBy) ? sortBy : "created_at";

String sql = "SELECT id, name, email FROM users ORDER BY " + sortColumn;
return jdbcTemplate.query(sql, new UserRowMapper());
```

---

### ✅ NamedParameterJdbcTemplate 範例（具名參數）

```java
String sql = "SELECT * FROM users WHERE status = :status";
return namedParameterJdbcTemplate.query(
    sql,
    Map.of("status", status),
    new UserRowMapper()
);
```

---

## 3️⃣ 錯誤作法（弱掃一定會報）

### ❌ 錯誤示範 1：字串拼接

```java
String sql = "SELECT * FROM users WHERE email = '" + email + "'";
jdbcTemplate.query(sql, new UserRowMapper());
```

**問題：**

* 攻擊者可傳入 `a@b.com' OR '1'='1`。
* 弱掃工具會報 SQL Injection。

---

### ❌ 錯誤示範 2：欄位名未驗證

```java
String sql = "SELECT * FROM users ORDER BY " + sortBy;
jdbcTemplate.query(sql, new UserRowMapper());
```

**問題：**

* 若 sortBy 傳入 `name; DROP TABLE users; --` 會造成嚴重風險。
* 必須採白名單判斷。

---

## 4️⃣ 安全程式設計建議

| 類別              | 建議作法                                                    |
| --------------- | ------------------------------------------------------- |
| **查詢語法**        | 一律使用 `?` 或 `:param` 參數化查詢                               |
| **排序欄位**        | 使用白名單映射，不接受自由輸入                                         |
| **SQL 來源**      | 不接受前端傳入 SQL 字串                                          |
| **字串處理**        | 僅用 `StringBuilder` 拼接固定語法，不拼使用者輸入                       |
| **DB 帳號權限**     | 使用最小權限帳號 (READ/WRITE 分離)                                |
| **例外處理**        | 不回傳完整 SQL 錯誤訊息給前端                                       |
| **審計**          | 記錄異常 SQL 嘗試、過長字串、特殊字元                                   |
| **檢測**          | 導入 SAST (SonarQube, Checkmarx) 與 DAST (OWASP ZAP, Burp) |
| **Code Review** | 檢查所有 SQL 是否使用參數化                                        |

---

## 5️⃣ 安全開發流程建議（SSDLC）

1. **設計階段：**

   * API 不允許傳入 SQL，僅允許 JSON 條件。
   * 定義可查詢欄位與條件白名單。

2. **開發階段：**

   * 所有 DB 查詢使用 `JdbcTemplate` 或 ORM 的 PreparedStatement。
   * 避免使用原生 Statement 或拼接 SQL。

3. **測試階段：**

   * 使用 OWASP ZAP / Burp Suite 進行弱掃。
   * 驗證 `' OR 1=1 --` 類測資不會影響查詢結果。

4. **部署階段：**

   * DB 帳號權限最小化。
   * 啟用 DB 防火牆與 SQL 審計。

5. **維運階段：**

   * 每季定期重新掃描弱點。
   * 所有新 raw SQL 需經 Code Review 安全審查。

---

## 6️⃣ 弱掃報告處理建議

若弱掃仍偵測 SQL Injection：

1. **確認是否使用 `?` 或具名參數。**
   若是，可註解標註：

   ```java
   // SAFE: Parameterized query using PreparedStatement
   ```

2. **附上安全說明文件**（本文件）給稽核或資安單位。
   說明 JdbcTemplate 預設使用 `PreparedStatement`，無 SQL 拼接風險。

3. **報告修正策略：**

   * 標記為「False Positive」
   * 附上程式證據與查詢語法說明

---

## 7️⃣ 附錄：安全範例摘要

| 功能    | 方法                                          |
| ----- | ------------------------------------------- |
| 查詢    | `findByEmail(String email)`                 |
| 插入    | `insertUser(String name, String email)`     |
| 更新    | `updateUserEmail(Long id, String newEmail)` |
| 刪除    | `deleteUser(Long id)`                       |
| 動態查詢  | `searchUsers(String name, String status)`   |
| 排序白名單 | `getUsersSorted(String sortBy)`             |

---

## ✅ 總結

> **核心口訣：**
> 「不拼 SQL、不信任輸入、使用 ? 或 :param、欄位要白名單。」

依本文件實作可確保：

* 通過 OWASP / DAST / SAST 弱掃工具。
* 滿足 SSDLC 資安要求。
* 提升程式可維護性與審計追溯性。




