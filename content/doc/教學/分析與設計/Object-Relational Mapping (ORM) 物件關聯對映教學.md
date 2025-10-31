# Object-Relational Mapping (ORM) 物件關聯對映教學手冊

## 目錄
1. [ORM 簡介](#1-orm-簡介)
   - [1.1 什麼是 ORM？](#11-什麼是-orm)
   - [1.2 為什麼需要 ORM？](#12-為什麼需要-orm)
   - [1.3 ORM 解決的問題](#13-orm-解決的問題)
   - [1.4 與 SQL/資料庫互動的關係](#14-與-sql資料庫互動的關係)
   - [1.5 小結](#15-小結)

2. [ORM 的基本概念](#2-orm-的基本概念)
   - [2.1 實體 (Entity)](#21-實體-entity)
   - [2.2 對應 (Mapping)](#22-對應-mapping)
   - [2.3 Session/EntityManager](#23-sessionentitymanager)
   - [2.4 Transaction (交易)](#24-transaction-交易)
   - [2.5 Lazy Loading vs Eager Loading](#25-lazy-loading-vs-eager-loading)
   - [2.6 小結](#26-小結)

3. [ORM 工具與框架簡介](#3-orm-工具與框架簡介)
   - [3.1 Java 生態系統](#31-java-生態系統)
   - [3.2 Python 生態系統](#32-python-生態系統)
   - [3.3 其他語言的 ORM 框架](#33-其他語言的-orm-框架)
   - [3.4 ORM 框架比較](#34-orm-框架比較)
   - [3.5 選擇 ORM 框架的考量因素](#35-選擇-orm-框架的考量因素)
   - [3.6 小結](#36-小結)

4. [安裝與設定](#4-安裝與設定)
   - [4.1 Java 環境設定 (Spring Boot + JPA)](#41-java-環境設定-spring-boot--jpa)
   - [4.2 Python 環境設定 (SQLAlchemy)](#42-python-環境設定-sqlalchemy)
   - [4.3 開發環境驗證](#43-開發環境驗證)
   - [4.4 常見安裝問題與解決方案](#44-常見安裝問題與解決方案)
   - [4.5 小結](#45-小結)

5. [基本 CRUD 範例](#5-基本-crud-範例)
   - [5.1 實體模型定義](#51-實體模型定義)
   - [5.2 Create (建立)](#52-create-建立)
   - [5.3 Read (查詢)](#53-read-查詢)
   - [5.4 Update (更新)](#54-update-更新)
   - [5.5 Delete (刪除)](#55-delete-刪除)
   - [5.6 完整的 CRUD 服務範例](#56-完整的-crud-服務範例)
   - [5.7 小結](#57-小結)

6. [關聯對映](#6-關聯對映)
   - [6.1 關聯類型概述](#61-關聯類型概述)
   - [6.2 One-to-One (一對一關聯)](#62-one-to-one-一對一關聯)
   - [6.3 One-to-Many (一對多關聯)](#63-one-to-many-一對多關聯)
   - [6.4 Many-to-Many (多對多關聯)](#64-many-to-many-多對多關聯)
   - [6.5 小結](#65-小結)

7. [進階主題](#7-進階主題)
   - [7.1 N+1 問題與解決方案](#71-n1-問題與解決方案)
   - [7.2 快取策略](#72-快取策略)
   - [7.3 效能監控與調校](#73-效能監控與調校)
   - [7.4 小結](#74-小結)

8. [專案最佳實務](#8-專案最佳實務)
   - [8.1 命名規則](#81-命名規則)
   - [8.2 錯誤處理](#82-錯誤處理)
   - [8.3 測試策略](#83-測試策略)
   - [8.4 小結](#84-小結)

9. [常見錯誤與排錯技巧](#9-常見錯誤與排錯技巧)
   - [9.1 LazyInitializationException](#91-lazyinitializationexception)
   - [9.2 N+1 查詢問題](#92-n1-查詢問題)
   - [9.3 資料庫連線問題](#93-資料庫連線問題)
   - [9.4 效能問題排錯](#94-效能問題排錯)
   - [9.5 資料一致性問題](#95-資料一致性問題)
   - [9.6 記憶體洩漏問題](#96-記憶體洩漏問題)
   - [9.7 常見錯誤檢查清單](#97-常見錯誤檢查清單)
   - [9.8 小結](#98-小結)

10. [認證考試重點與練習題](#10-認證考試重點與練習題)
    - [10.1 Java JPA/Hibernate 認證重點](#101-java-jpahibernate-認證重點)
    - [10.2 Python SQLAlchemy 認證重點](#102-python-sqlalchemy-認證重點)
    - [10.3 認證考試準備策略](#103-認證考試準備策略)
    - [10.4 模擬考試題目](#104-模擬考試題目)
    - [10.5 小結](#105-小結)

11. [結論與學習資源](#11-結論與學習資源)
    - [11.1 學習總結](#111-學習總結)
    - [11.2 推薦學習資源](#112-推薦學習資源)
    - [11.3 持續學習建議](#113-持續學習建議)
    - [11.4 實務專案建議](#114-實務專案建議)
    - [11.5 職涯發展建議](#115-職涯發展建議)
    - [11.6 最終建議](#116-最終建議)

12. [檢查清單](#12-檢查清單)
    - [12.1 新專案啟動檢查清單](#121-新專案啟動檢查清單)
    - [12.2 開發階段檢查清單](#122-開發階段檢查清單)
    - [12.3 測試階段檢查清單](#123-測試階段檢查清單)
    - [12.4 部署前檢查清單](#124-部署前檢查清單)
    - [12.5 維運階段檢查清單](#125-維運階段檢查清單)
    - [12.6 故障排除檢查清單](#126-故障排除檢查清單)

---

## 1. ORM 簡介

### 1.1 什麼是 ORM？

**Object-Relational Mapping (ORM)** 是一種程式設計技術，用於在物件導向程式語言和關聯式資料庫之間建立映射關係。簡單來說，ORM 讓開發者可以使用物件導向的方式來操作資料庫，而不需要直接撰寫 SQL 語句。

### 1.2 為什麼需要 ORM？

```mermaid
graph TD
    A[物件導向程式] --> B[阻抗不匹配問題]
    C[關聯式資料庫] --> B
    B --> D[ORM 解決方案]
    D --> E[自動映射]
    D --> F[減少重複程式碼]
    D --> G[提高開發效率]
    D --> H[降低維護成本]
```

#### 傳統開發面臨的問題：

1. **阻抗不匹配 (Impedance Mismatch)**
   - 物件導向：封裝、繼承、多型
   - 關聯式資料庫：表格、行、列

2. **重複性程式碼**
   - 大量的 SQL 語句
   - 資料轉換邏輯
   - 連線管理

3. **維護困難**
   - 資料庫結構變更影響程式碼
   - SQL 語句散布在各處
   - 除錯困難

### 1.3 ORM 解決的問題

#### 1.3.1 自動化資料映射
```java
// 傳統 JDBC 方式
String sql = "SELECT id, name, email FROM users WHERE id = ?";
PreparedStatement stmt = connection.prepareStatement(sql);
stmt.setInt(1, userId);
ResultSet rs = stmt.executeQuery();
if (rs.next()) {
    User user = new User();
    user.setId(rs.getInt("id"));
    user.setName(rs.getString("name"));
    user.setEmail(rs.getString("email"));
}

// ORM 方式
User user = entityManager.find(User.class, userId);
```

#### 1.3.2 資料庫抽象化
- 支援多種資料庫（MySQL、PostgreSQL、Oracle 等）
- 資料庫方言自動處理
- 易於切換資料庫供應商

#### 1.3.3 物件關聯處理
- 自動處理外鍵關係
- 延遲載入 (Lazy Loading)
- 快取機制

### 1.4 與 SQL/資料庫互動的關係

```mermaid
sequenceDiagram
    participant App as 應用程式
    participant ORM as ORM 框架
    participant DB as 資料庫
    
    App->>ORM: 呼叫物件方法
    ORM->>ORM: 生成 SQL 語句
    ORM->>DB: 執行 SQL
    DB->>ORM: 回傳結果
    ORM->>ORM: 對映為物件
    ORM->>App: 回傳物件
```

### 1.5 小結

- ORM 是連接物件導向程式語言與關聯式資料庫的橋樑
- 解決了阻抗不匹配問題，提高開發效率
- 提供資料庫抽象化，增強程式可移植性
- 自動處理資料映射和關聯關係

**注意事項：**
- ORM 不是萬能的，複雜查詢仍可能需要原生 SQL
- 需要了解底層 SQL 執行機制，避免效能問題
- 適當的設定和最佳化是必要的

---

## 2. ORM 的基本概念

### 2.1 實體 (Entity)

**實體**是 ORM 中的核心概念，代表資料庫中的一個表格。每個實體類別對應一個資料庫表格。

#### Java 實體範例
```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "username", unique = true, nullable = false)
    private String username;
    
    @Column(name = "email")
    private String email;
    
    @Temporal(TemporalType.TIMESTAMP)
    @Column(name = "created_at")
    private Date createdAt;
    
    // 建構函式、getter、setter...
}
```

#### Python 實體範例
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
```

### 2.2 對應 (Mapping)

對應定義了物件屬性與資料庫欄位之間的關係。

```mermaid
graph LR
    A[Java/Python 類別] --> B[ORM 對應]
    B --> C[資料庫表格]
    
    A1[屬性 id] --> B1[主鍵對應] --> C1[PRIMARY KEY]
    A2[屬性 username] --> B2[欄位對應] --> C2[VARCHAR]
    A3[屬性 createdAt] --> B3[型別對應] --> C3[DATETIME]
```

### 2.3 Session/EntityManager

**Session** (Hibernate) 或 **EntityManager** (JPA) 是 ORM 與資料庫之間的主要介面。

#### Java (JPA) 範例
```java
@PersistenceContext
private EntityManager entityManager;

public void saveUser(User user) {
    entityManager.persist(user);
}

public User findUser(Long id) {
    return entityManager.find(User.class, id);
}
```

#### Python (SQLAlchemy) 範例
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def save_user(user):
    session.add(user)
    session.commit()

def find_user(user_id):
    return session.query(User).filter(User.id == user_id).first()
```

### 2.4 Transaction (交易)

**交易**確保資料的一致性和完整性，遵循 ACID 特性。

```mermaid
graph TD
    A[開始交易] --> B[執行操作1]
    B --> C[執行操作2]
    C --> D[執行操作3]
    D --> E{所有操作成功?}
    E -->|是| F[提交交易]
    E -->|否| G[回滾交易]
    F --> H[交易完成]
    G --> H
```

#### Java 交易範例
```java
@Transactional
public void transferMoney(Long fromId, Long toId, BigDecimal amount) {
    Account fromAccount = accountRepository.findById(fromId);
    Account toAccount = accountRepository.findById(toId);
    
    fromAccount.withdraw(amount);
    toAccount.deposit(amount);
    
    accountRepository.save(fromAccount);
    accountRepository.save(toAccount);
    // 如果任何步驟失敗，整個交易將回滾
}
```

#### Python 交易範例
```python
def transfer_money(from_id, to_id, amount):
    try:
        from_account = session.query(Account).filter(Account.id == from_id).first()
        to_account = session.query(Account).filter(Account.id == to_id).first()
        
        from_account.withdraw(amount)
        to_account.deposit(amount)
        
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
```

### 2.5 Lazy Loading vs Eager Loading

#### 2.5.1 Lazy Loading (延遲載入)
```java
@Entity
public class User {
    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY)
    private List<Order> orders; // 只有在實際存取時才載入
}

// 使用時
User user = userRepository.findById(1L);
// 此時 orders 尚未載入
List<Order> orders = user.getOrders(); // 現在才執行 SQL 載入 orders
```

#### 2.5.2 Eager Loading (立即載入)
```java
@Entity
public class User {
    @OneToMany(mappedBy = "user", fetch = FetchType.EAGER)
    private List<Order> orders; // 立即載入
}

// 使用時
User user = userRepository.findById(1L); // orders 同時載入
```

#### 載入策略比較

| 特性 | Lazy Loading | Eager Loading |
|------|-------------|---------------|
| 記憶體使用 | 較少 | 較多 |
| 載入速度 | 按需載入 | 一次載入 |
| N+1 問題 | 可能發生 | 較少發生 |
| 適用場景 | 大型物件關聯 | 小型必要關聯 |

### 2.6 小結

- **實體**：代表資料庫表格的 Java/Python 類別
- **對應**：定義物件屬性與資料庫欄位的關係
- **Session/EntityManager**：ORM 與資料庫的主要介面
- **交易**：確保資料一致性的機制
- **載入策略**：控制關聯資料的載入時機

**實務建議：**
- 優先使用 Lazy Loading，避免不必要的資料載入
- 適當使用交易確保資料一致性
- 理解 Session 的生命週期，避免 LazyInitializationException

---

## 3. ORM 工具與框架簡介

### 3.1 Java 生態系統

#### 3.1.1 JPA (Java Persistence API)
JPA 是 Java 的官方持久化規範，定義了標準的 ORM 介面。

**特色：**
- 官方標準規範
- 供應商中立
- 註解驅動
- JPQL 查詢語言

#### 3.1.2 Hibernate
Hibernate 是最流行的 JPA 實作之一。

```mermaid
graph TD
    A[應用程式] --> B[JPA API]
    B --> C[Hibernate 實作]
    C --> D[JDBC]
    D --> E[資料庫]
    
    F[Spring Data JPA] --> B
    G[其他 JPA 實作] --> B
```

**Hibernate 特色：**
- 成熟穩定
- 豐富的功能
- 優秀的快取機制
- 支援多種資料庫

#### 3.1.3 Spring Data JPA
Spring Data JPA 建構在 JPA 之上，提供更簡潔的開發體驗。

```java
// 傳統 JPA Repository
@Repository
public class UserRepository {
    @PersistenceContext
    private EntityManager entityManager;
    
    public List<User> findByEmail(String email) {
        return entityManager
            .createQuery("SELECT u FROM User u WHERE u.email = :email", User.class)
            .setParameter("email", email)
            .getResultList();
    }
}

// Spring Data JPA Repository
public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByEmail(String email); // 方法名稱自動生成查詢
    
    @Query("SELECT u FROM User u WHERE u.username LIKE %?1%")
    List<User> findByUsernameContaining(String username);
}
```

### 3.2 Python 生態系統

#### 3.2.1 SQLAlchemy
SQLAlchemy 是 Python 最流行的 ORM 框架。

```mermaid
graph TD
    A[應用程式] --> B[SQLAlchemy ORM]
    B --> C[SQLAlchemy Core]
    C --> D[Connection Pool]
    D --> E[Database Adapter]
    E --> F[資料庫]
```

**SQLAlchemy 特色：**
- 靈活性高
- 支援多種設計模式
- 優秀的效能
- 豐富的資料型別支援

#### SQLAlchemy 範例
```python
# 宣告式模型
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="orders")
```

#### 3.2.2 Django ORM
Django 內建的 ORM 框架，與 Django 框架緊密整合。

```python
# Django 模型
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'

# 使用方式
users = User.objects.filter(username__startswith='john')
user = User.objects.get(id=1)
```

### 3.3 其他語言的 ORM 框架

#### 3.3.1 .NET - Entity Framework
```csharp
public class User
{
    public int Id { get; set; }
    public string Username { get; set; }
    public List<Order> Orders { get; set; }
}

public class ApplicationDbContext : DbContext
{
    public DbSet<User> Users { get; set; }
    public DbSet<Order> Orders { get; set; }
}
```

#### 3.3.2 Node.js - TypeORM
```typescript
@Entity()
export class User {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ unique: true })
    username: string;

    @OneToMany(() => Order, order => order.user)
    orders: Order[];
}
```

### 3.4 ORM 框架比較

| 框架 | 語言 | 學習曲線 | 效能 | 社群支援 | 企業應用 |
|------|------|----------|------|----------|----------|
| Hibernate/JPA | Java | 中等 | 高 | 優秀 | 優秀 |
| Spring Data JPA | Java | 容易 | 高 | 優秀 | 優秀 |
| SQLAlchemy | Python | 困難 | 非常高 | 優秀 | 優秀 |
| Django ORM | Python | 容易 | 中等 | 優秀 | 良好 |
| Entity Framework | C# | 容易 | 高 | 優秀 | 優秀 |

### 3.5 選擇 ORM 框架的考量因素

```mermaid
mindmap
  root((ORM 選擇))
    技術因素
      效能需求
      學習曲線
      框架成熟度
      社群支援
    專案因素
      團隊技能
      專案規模
      維護需求
      長期規劃
    環境因素
      現有技術棧
      資料庫類型
      部署環境
      整合需求
```

### 3.6 小結

- **Java**：JPA/Hibernate 為主流，Spring Data JPA 簡化開發
- **Python**：SQLAlchemy 功能強大，Django ORM 易於使用
- **選擇標準**：考慮團隊技能、專案需求、效能要求
- **學習建議**：先掌握一種框架的深度，再學習其他框架

**實務建議：**
- 新專案優先考慮主流框架
- 重視官方文件和社群支援
- 考慮框架的長期維護和升級路徑
- 評估團隊的學習成本和開發效率

---

## 4. 安裝與設定

### 4.1 Java 環境設定 (Spring Boot + JPA)

#### 4.1.1 Maven 依賴設定

```xml
<!-- pom.xml -->
<project>
    <properties>
        <java.version>17</java.version>
        <spring.boot.version>3.1.0</spring.boot.version>
    </properties>
    
    <dependencies>
        <!-- Spring Boot Starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        
        <!-- 資料庫驅動 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>
        
        <!-- H2 資料庫 (測試用) -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>test</scope>
        </dependency>
        
        <!-- Validation -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
    </dependencies>
</project>
```

#### 4.1.2 應用程式設定

```yaml
# application.yml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/tutorial_db?serverTimezone=UTC
    username: tutorial_user
    password: tutorial_password
    driver-class-name: com.mysql.cj.jdbc.Driver
  
  jpa:
    hibernate:
      ddl-auto: update  # 開發環境用，生產環境建議用 validate
    show-sql: true      # 顯示 SQL 語句
    format-sql: true    # 格式化 SQL 語句
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQL8Dialect
        format_sql: true
        use_sql_comments: true
  
  logging:
    level:
      org.hibernate.SQL: DEBUG
      org.hibernate.type.descriptor.sql.BasicBinder: TRACE
```

#### 4.1.3 資料庫初始化腳本

```sql
-- schema.sql
CREATE DATABASE IF NOT EXISTS tutorial_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'tutorial_user'@'localhost' 
IDENTIFIED BY 'tutorial_password';

GRANT ALL PRIVILEGES ON tutorial_db.* 
TO 'tutorial_user'@'localhost';

FLUSH PRIVILEGES;
```

### 4.2 Python 環境設定 (SQLAlchemy)

#### 4.2.1 套件安裝

```bash
# 建立虛擬環境
python -m venv orm_tutorial
source orm_tutorial/bin/activate  # Linux/Mac
# 或
orm_tutorial\Scripts\activate     # Windows

# 安裝必要套件
pip install sqlalchemy
pip install mysql-connector-python  # MySQL 驅動
pip install alembic                 # 資料庫遷移工具
pip install python-dotenv           # 環境變數管理
```

#### 4.2.2 requirements.txt

```text
sqlalchemy==2.0.19
mysql-connector-python==8.1.0
alembic==1.11.1
python-dotenv==1.0.0
pytest==7.4.0
pytest-cov==4.1.0
```

#### 4.2.3 資料庫設定

```python
# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# 資料庫 URL 設定
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "mysql+mysqlconnector://tutorial_user:tutorial_password@localhost:3306/tutorial_db"
)

# 建立引擎
engine = create_engine(
    DATABASE_URL,
    echo=True,  # 顯示 SQL 語句
    pool_pre_ping=True,  # 連線檢查
    pool_recycle=3600    # 連線回收時間
)

# Session 工廠
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基礎模型類別
Base = declarative_base()

# 依賴注入函數
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### 4.2.4 環境變數設定

```bash
# .env
DATABASE_URL=mysql+mysqlconnector://tutorial_user:tutorial_password@localhost:3306/tutorial_db
DEBUG=True
LOG_LEVEL=INFO
```

### 4.3 開發環境驗證

#### 4.3.1 Java 環境測試

```java
// DatabaseConnectionTest.java
@SpringBootTest
public class DatabaseConnectionTest {
    
    @Autowired
    private DataSource dataSource;
    
    @Test
    public void testDatabaseConnection() throws SQLException {
        try (Connection connection = dataSource.getConnection()) {
            assertThat(connection).isNotNull();
            assertThat(connection.isValid(1)).isTrue();
        }
    }
}
```

#### 4.3.2 Python 環境測試

```python
# test_database.py
import pytest
from database import engine, SessionLocal, Base

def test_database_connection():
    """測試資料庫連線"""
    try:
        # 測試連線
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            assert result.fetchone()[0] == 1
        
        # 測試 Session
        session = SessionLocal()
        try:
            session.execute("SELECT 1")
        finally:
            session.close()
            
    except Exception as e:
        pytest.fail(f"資料庫連線失敗: {e}")

if __name__ == "__main__":
    test_database_connection()
    print("資料庫連線測試成功！")
```

### 4.4 常見安裝問題與解決方案

#### 4.4.1 Java 常見問題

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| 找不到驅動程式 | 缺少資料庫驅動依賴 | 添加對應的資料庫驅動依賴 |
| 連線被拒絕 | 資料庫服務未啟動 | 檢查資料庫服務狀態 |
| 字元編碼問題 | URL 參數設定不正確 | 添加 `?serverTimezone=UTC&characterEncoding=utf8` |
| LazyInitializationException | Session 已關閉 | 使用 `@Transactional` 或調整 fetch 策略 |

#### 4.4.2 Python 常見問題

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| 模組找不到 | 套件未安裝 | `pip install <package_name>` |
| 連線逾時 | 網路或資料庫設定問題 | 檢查防火牆和資料庫設定 |
| 權限被拒絕 | 資料庫用戶權限不足 | 檢查用戶權限設定 |
| 版本衝突 | 套件版本不相容 | 使用虛擬環境隔離依賴 |

### 4.5 小結

- **Java**：使用 Spring Boot + JPA 簡化設定
- **Python**：使用 SQLAlchemy + Alembic 建立完整的資料存取層
- **設定重點**：資料庫連線、日誌輸出、環境區分
- **測試重要性**：確保環境設定正確

**實務建議：**
- 使用環境變數管理敏感資訊
- 開發、測試、生產環境分離設定
- 建立資料庫連線測試確保環境正確
- 善用 Docker 統一開發環境

---

## 5. 基本 CRUD 範例

### 5.1 實體模型定義

#### 5.1.1 Java 實體模型

```java
// User.java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "username", unique = true, nullable = false, length = 50)
    private String username;
    
    @Column(name = "email", nullable = false, length = 100)
    private String email;
    
    @Column(name = "full_name", length = 100)
    private String fullName;
    
    @Enumerated(EnumType.STRING)
    @Column(name = "status")
    private UserStatus status = UserStatus.ACTIVE;
    
    @CreationTimestamp
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;
    
    @UpdateTimestamp
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;
    
    // 建構函式
    public User() {}
    
    public User(String username, String email, String fullName) {
        this.username = username;
        this.email = email;
        this.fullName = fullName;
    }
    
    // Getter 和 Setter
    // ... 省略 getter/setter 方法
    
    @Override
    public String toString() {
        return String.format("User{id=%d, username='%s', email='%s'}", 
                           id, username, email);
    }
}

// UserStatus.java
public enum UserStatus {
    ACTIVE, INACTIVE, SUSPENDED
}
```

#### 5.1.2 Python 實體模型

```python
# models.py
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class UserStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), nullable=False)
    full_name = Column(String(100))
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, username, email, full_name=None):
        self.username = username
        self.email = email
        self.full_name = full_name
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'status': self.status.value if self.status else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
```

### 5.2 Create (建立)

#### 5.2.1 Java - 建立資料

```java
// UserRepository.java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
    Optional<User> findByEmail(String email);
    List<User> findByStatus(UserStatus status);
}

// UserService.java
@Service
@Transactional
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    public User createUser(String username, String email, String fullName) {
        // 檢查用戶名是否已存在
        if (userRepository.findByUsername(username).isPresent()) {
            throw new IllegalArgumentException("用戶名已存在: " + username);
        }
        
        // 檢查郵箱是否已存在
        if (userRepository.findByEmail(email).isPresent()) {
            throw new IllegalArgumentException("郵箱已存在: " + email);
        }
        
        User user = new User(username, email, fullName);
        return userRepository.save(user);
    }
    
    public List<User> createUsers(List<User> users) {
        return userRepository.saveAll(users);
    }
}

// 使用範例
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody @Valid CreateUserRequest request) {
        User user = userService.createUser(
            request.getUsername(), 
            request.getEmail(), 
            request.getFullName()
        );
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}
```

#### 5.2.2 Python - 建立資料

```python
# user_service.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import User, UserStatus
from database import SessionLocal

class UserService:
    def __init__(self):
        self.db = SessionLocal()
    
    def create_user(self, username: str, email: str, full_name: str = None) -> User:
        """建立新用戶"""
        try:
            # 檢查用戶名是否已存在
            existing_user = self.db.query(User).filter(User.username == username).first()
            if existing_user:
                raise ValueError(f"用戶名已存在: {username}")
            
            # 檢查郵箱是否已存在
            existing_email = self.db.query(User).filter(User.email == email).first()
            if existing_email:
                raise ValueError(f"郵箱已存在: {email}")
            
            # 建立新用戶
            user = User(username=username, email=email, full_name=full_name)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)  # 重新載入以獲取生成的 ID
            return user
            
        except IntegrityError as e:
            self.db.rollback()
            raise ValueError(f"資料完整性錯誤: {str(e)}")
        except Exception as e:
            self.db.rollback()
            raise e
    
    def create_users_batch(self, users_data: list) -> list:
        """批次建立用戶"""
        try:
            users = [User(**user_data) for user_data in users_data]
            self.db.add_all(users)
            self.db.commit()
            return users
        except Exception as e:
            self.db.rollback()
            raise e
    
    def __del__(self):
        if hasattr(self, 'db'):
            self.db.close()

# 使用範例
def example_create_user():
    user_service = UserService()
    
    # 建立單一用戶
    try:
        user = user_service.create_user(
            username="john_doe",
            email="john@example.com",
            full_name="John Doe"
        )
        print(f"用戶建立成功: {user}")
    except ValueError as e:
        print(f"建立失敗: {e}")
```

### 5.3 Read (查詢)

#### 5.3.1 Java - 查詢資料

```java
// UserService.java (查詢方法)
@Service
@Transactional(readOnly = true)
public class UserService {
    
    // 根據 ID 查詢
    public Optional<User> findById(Long id) {
        return userRepository.findById(id);
    }
    
    // 根據用戶名查詢
    public Optional<User> findByUsername(String username) {
        return userRepository.findByUsername(username);
    }
    
    // 查詢所有用戶
    public List<User> findAllUsers() {
        return userRepository.findAll();
    }
    
    // 分頁查詢
    public Page<User> findUsersWithPagination(int page, int size) {
        Pageable pageable = PageRequest.of(page, size, Sort.by("createdAt").descending());
        return userRepository.findAll(pageable);
    }
    
    // 條件查詢
    public List<User> findActiveUsers() {
        return userRepository.findByStatus(UserStatus.ACTIVE);
    }
    
    // 複雜查詢
    @Query("SELECT u FROM User u WHERE u.email LIKE %:domain%")
    public List<User> findUsersByEmailDomain(@Param("domain") String domain);
    
    // 統計查詢
    public long countActiveUsers() {
        return userRepository.countByStatus(UserStatus.ACTIVE);
    }
}

// 使用範例
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        return userService.findById(id)
                .map(user -> ResponseEntity.ok(user))
                .orElse(ResponseEntity.notFound().build());
    }
    
    @GetMapping
    public ResponseEntity<Page<User>> getUsers(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        Page<User> users = userService.findUsersWithPagination(page, size);
        return ResponseEntity.ok(users);
    }
}
```

#### 5.3.2 Python - 查詢資料

```python
# user_service.py (查詢方法)
from typing import List, Optional
from sqlalchemy import func, desc

class UserService:
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        """根據 ID 查詢用戶"""
        return self.db.query(User).filter(User.id == user_id).first()
    
    def find_by_username(self, username: str) -> Optional[User]:
        """根據用戶名查詢用戶"""
        return self.db.query(User).filter(User.username == username).first()
    
    def find_all_users(self) -> List[User]:
        """查詢所有用戶"""
        return self.db.query(User).all()
    
    def find_users_with_pagination(self, page: int = 1, size: int = 10) -> dict:
        """分頁查詢用戶"""
        offset = (page - 1) * size
        users = (self.db.query(User)
                .order_by(desc(User.created_at))
                .offset(offset)
                .limit(size)
                .all())
        
        total = self.db.query(func.count(User.id)).scalar()
        
        return {
            'users': users,
            'total': total,
            'page': page,
            'size': size,
            'total_pages': (total + size - 1) // size
        }
    
    def find_active_users(self) -> List[User]:
        """查詢活躍用戶"""
        return self.db.query(User).filter(User.status == UserStatus.ACTIVE).all()
    
    def find_users_by_email_domain(self, domain: str) -> List[User]:
        """根據郵箱域名查詢用戶"""
        return self.db.query(User).filter(User.email.like(f'%{domain}%')).all()
    
    def count_active_users(self) -> int:
        """統計活躍用戶數量"""
        return self.db.query(func.count(User.id)).filter(User.status == UserStatus.ACTIVE).scalar()
    
    def search_users(self, keyword: str) -> List[User]:
        """搜尋用戶（用戶名或全名）"""
        return (self.db.query(User)
                .filter(
                    (User.username.like(f'%{keyword}%')) |
                    (User.full_name.like(f'%{keyword}%'))
                )
                .all())

# 使用範例
def example_read_users():
    user_service = UserService()
    
    # 查詢單一用戶
    user = user_service.find_by_id(1)
    if user:
        print(f"找到用戶: {user}")
    else:
        print("用戶不存在")
    
    # 分頁查詢
    result = user_service.find_users_with_pagination(page=1, size=5)
    print(f"總共 {result['total']} 位用戶，當前頁面有 {len(result['users'])} 位")
    
    # 搜尋用戶
    users = user_service.search_users("john")
    print(f"搜尋結果: {len(users)} 位用戶")
```

### 5.4 Update (更新)

#### 5.4.1 Java - 更新資料

```java
// UserService.java (更新方法)
@Service
@Transactional
public class UserService {
    
    public User updateUser(Long id, String email, String fullName) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("用戶不存在: " + id));
        
        // 檢查郵箱是否被其他用戶使用
        userRepository.findByEmail(email)
                .filter(existingUser -> !existingUser.getId().equals(id))
                .ifPresent(existingUser -> {
                    throw new IllegalArgumentException("郵箱已被使用: " + email);
                });
        
        user.setEmail(email);
        user.setFullName(fullName);
        
        return userRepository.save(user);
    }
    
    public User updateUserStatus(Long id, UserStatus status) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("用戶不存在: " + id));
        
        user.setStatus(status);
        return userRepository.save(user);
    }
    
    // 批次更新
    public List<User> updateUsersStatus(List<Long> userIds, UserStatus status) {
        List<User> users = userRepository.findAllById(userIds);
        users.forEach(user -> user.setStatus(status));
        return userRepository.saveAll(users);
    }
    
    // 條件更新
    @Modifying
    @Query("UPDATE User u SET u.status = :status WHERE u.createdAt < :cutoffDate")
    public int updateInactiveUsers(@Param("status") UserStatus status, 
                                 @Param("cutoffDate") LocalDateTime cutoffDate) {
        return userRepository.updateInactiveUsers(status, cutoffDate);
    }
}

// 使用範例
@PutMapping("/{id}")
public ResponseEntity<User> updateUser(@PathVariable Long id, 
                                     @RequestBody @Valid UpdateUserRequest request) {
    try {
        User updatedUser = userService.updateUser(id, request.getEmail(), request.getFullName());
        return ResponseEntity.ok(updatedUser);
    } catch (EntityNotFoundException e) {
        return ResponseEntity.notFound().build();
    }
}
```

#### 5.4.2 Python - 更新資料

```python
# user_service.py (更新方法)
class UserService:
    
    def update_user(self, user_id: int, email: str = None, full_name: str = None) -> User:
        """更新用戶資訊"""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if not user:
                raise ValueError(f"用戶不存在: {user_id}")
            
            # 檢查郵箱是否被其他用戶使用
            if email:
                existing_user = (self.db.query(User)
                               .filter(User.email == email, User.id != user_id)
                               .first())
                if existing_user:
                    raise ValueError(f"郵箱已被使用: {email}")
                user.email = email
            
            if full_name is not None:
                user.full_name = full_name
            
            # 更新時間會自動設定
            self.db.commit()
            self.db.refresh(user)
            return user
            
        except Exception as e:
            self.db.rollback()
            raise e
    
    def update_user_status(self, user_id: int, status: UserStatus) -> User:
        """更新用戶狀態"""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if not user:
                raise ValueError(f"用戶不存在: {user_id}")
            
            user.status = status
            self.db.commit()
            self.db.refresh(user)
            return user
            
        except Exception as e:
            self.db.rollback()
            raise e
    
    def update_users_status_batch(self, user_ids: List[int], status: UserStatus) -> int:
        """批次更新用戶狀態"""
        try:
            updated_count = (self.db.query(User)
                           .filter(User.id.in_(user_ids))
                           .update({User.status: status}, synchronize_session=False))
            self.db.commit()
            return updated_count
            
        except Exception as e:
            self.db.rollback()
            raise e
    
    def update_inactive_users(self, cutoff_date, status: UserStatus) -> int:
        """條件更新：將特定日期前的用戶設為非活躍"""
        try:
            updated_count = (self.db.query(User)
                           .filter(User.created_at < cutoff_date)
                           .update({User.status: status}, synchronize_session=False))
            self.db.commit()
            return updated_count
            
        except Exception as e:
            self.db.rollback()
            raise e

# 使用範例
def example_update_user():
    user_service = UserService()
    
    try:
        # 更新用戶資訊
        updated_user = user_service.update_user(
            user_id=1,
            email="new_email@example.com",
            full_name="New Full Name"
        )
        print(f"用戶更新成功: {updated_user}")
        
        # 更新用戶狀態
        user_service.update_user_status(1, UserStatus.INACTIVE)
        print("用戶狀態更新成功")
        
    except ValueError as e:
        print(f"更新失敗: {e}")
```

### 5.5 Delete (刪除)

#### 5.5.1 Java - 刪除資料

```java
// UserService.java (刪除方法)
@Service
@Transactional
public class UserService {
    
    public void deleteUser(Long id) {
        if (!userRepository.existsById(id)) {
            throw new EntityNotFoundException("用戶不存在: " + id);
        }
        userRepository.deleteById(id);
    }
    
    public void deleteUserSoft(Long id) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("用戶不存在: " + id));
        
        user.setStatus(UserStatus.INACTIVE);
        userRepository.save(user);
    }
    
    // 批次刪除
    public void deleteUsers(List<Long> userIds) {
        List<User> users = userRepository.findAllById(userIds);
        if (users.size() != userIds.size()) {
            throw new IllegalArgumentException("部分用戶不存在");
        }
        userRepository.deleteAll(users);
    }
    
    // 條件刪除
    @Modifying
    @Query("DELETE FROM User u WHERE u.status = :status AND u.createdAt < :cutoffDate")
    public int deleteInactiveUsers(@Param("status") UserStatus status, 
                                 @Param("cutoffDate") LocalDateTime cutoffDate) {
        return userRepository.deleteInactiveUsers(status, cutoffDate);
    }
}

// 使用範例
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    try {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    } catch (EntityNotFoundException e) {
        return ResponseEntity.notFound().build();
    }
}
```

#### 5.5.2 Python - 刪除資料

```python
# user_service.py (刪除方法)
class UserService:
    
    def delete_user(self, user_id: int) -> bool:
        """刪除用戶"""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if not user:
                raise ValueError(f"用戶不存在: {user_id}")
            
            self.db.delete(user)
            self.db.commit()
            return True
            
        except Exception as e:
            self.db.rollback()
            raise e
    
    def delete_user_soft(self, user_id: int) -> User:
        """軟刪除用戶（設為非活躍狀態）"""
        return self.update_user_status(user_id, UserStatus.INACTIVE)
    
    def delete_users_batch(self, user_ids: List[int]) -> int:
        """批次刪除用戶"""
        try:
            deleted_count = (self.db.query(User)
                           .filter(User.id.in_(user_ids))
                           .delete(synchronize_session=False))
            self.db.commit()
            return deleted_count
            
        except Exception as e:
            self.db.rollback()
            raise e
    
    def delete_inactive_users(self, cutoff_date) -> int:
        """條件刪除：刪除特定日期前的非活躍用戶"""
        try:
            deleted_count = (self.db.query(User)
                           .filter(
                               User.status == UserStatus.INACTIVE,
                               User.created_at < cutoff_date
                           )
                           .delete(synchronize_session=False))
            self.db.commit()
            return deleted_count
            
        except Exception as e:
            self.db.rollback()
            raise e

# 使用範例
def example_delete_user():
    user_service = UserService()
    
    try:
        # 刪除單一用戶
        success = user_service.delete_user(1)
        if success:
            print("用戶刪除成功")
        
        # 批次刪除
        deleted_count = user_service.delete_users_batch([2, 3, 4])
        print(f"成功刪除 {deleted_count} 位用戶")
        
    except ValueError as e:
        print(f"刪除失敗: {e}")
```

### 5.6 完整的 CRUD 服務範例

#### 5.6.1 Java 完整服務

```java
// UserCrudService.java
@Service
@Transactional
@Slf4j
public class UserCrudService {
    
    @Autowired
    private UserRepository userRepository;
    
    // CREATE
    public User create(CreateUserRequest request) {
        log.info("建立用戶: {}", request.getUsername());
        
        validateUniqueUsername(request.getUsername());
        validateUniqueEmail(request.getEmail());
        
        User user = new User(request.getUsername(), request.getEmail(), request.getFullName());
        User savedUser = userRepository.save(user);
        
        log.info("用戶建立成功: {}", savedUser.getId());
        return savedUser;
    }
    
    // READ
    @Transactional(readOnly = true)
    public UserDto getById(Long id) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("用戶不存在: " + id));
        return convertToDto(user);
    }
    
    // UPDATE
    public UserDto update(Long id, UpdateUserRequest request) {
        log.info("更新用戶: {}", id);
        
        User user = userRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("用戶不存在: " + id));
        
        if (!user.getEmail().equals(request.getEmail())) {
            validateUniqueEmail(request.getEmail());
            user.setEmail(request.getEmail());
        }
        
        user.setFullName(request.getFullName());
        User updatedUser = userRepository.save(user);
        
        log.info("用戶更新成功: {}", id);
        return convertToDto(updatedUser);
    }
    
    // DELETE
    public void delete(Long id) {
        log.info("刪除用戶: {}", id);
        
        if (!userRepository.existsById(id)) {
            throw new EntityNotFoundException("用戶不存在: " + id);
        }
        
        userRepository.deleteById(id);
        log.info("用戶刪除成功: {}", id);
    }
    
    // 工具方法
    private void validateUniqueUsername(String username) {
        if (userRepository.findByUsername(username).isPresent()) {
            throw new IllegalArgumentException("用戶名已存在: " + username);
        }
    }
    
    private void validateUniqueEmail(String email) {
        if (userRepository.findByEmail(email).isPresent()) {
            throw new IllegalArgumentException("郵箱已存在: " + email);
        }
    }
    
    private UserDto convertToDto(User user) {
        return new UserDto(
            user.getId(),
            user.getUsername(),
            user.getEmail(),
            user.getFullName(),
            user.getStatus(),
            user.getCreatedAt(),
            user.getUpdatedAt()
        );
    }
}
```

#### 5.6.2 Python 完整服務

```python
# user_crud_service.py
import logging
from typing import Optional, List
from datetime import datetime
from models import User, UserStatus
from database import SessionLocal

logger = logging.getLogger(__name__)

class UserCrudService:
    def __init__(self):
        self.db = SessionLocal()
    
    def create(self, username: str, email: str, full_name: str = None) -> dict:
        """建立用戶"""
        logger.info(f"建立用戶: {username}")
        
        try:
            self._validate_unique_username(username)
            self._validate_unique_email(email)
            
            user = User(username=username, email=email, full_name=full_name)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            
            logger.info(f"用戶建立成功: {user.id}")
            return self._to_dict(user)
            
        except Exception as e:
            self.db.rollback()
            logger.error(f"建立用戶失敗: {str(e)}")
            raise e
    
    def get_by_id(self, user_id: int) -> dict:
        """根據 ID 查詢用戶"""
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError(f"用戶不存在: {user_id}")
        return self._to_dict(user)
    
    def update(self, user_id: int, email: str = None, full_name: str = None) -> dict:
        """更新用戶"""
        logger.info(f"更新用戶: {user_id}")
        
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if not user:
                raise ValueError(f"用戶不存在: {user_id}")
            
            if email and email != user.email:
                self._validate_unique_email(email, exclude_id=user_id)
                user.email = email
            
            if full_name is not None:
                user.full_name = full_name
            
            self.db.commit()
            self.db.refresh(user)
            
            logger.info(f"用戶更新成功: {user_id}")
            return self._to_dict(user)
            
        except Exception as e:
            self.db.rollback()
            logger.error(f"更新用戶失敗: {str(e)}")
            raise e
    
    def delete(self, user_id: int) -> bool:
        """刪除用戶"""
        logger.info(f"刪除用戶: {user_id}")
        
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if not user:
                raise ValueError(f"用戶不存在: {user_id}")
            
            self.db.delete(user)
            self.db.commit()
            
            logger.info(f"用戶刪除成功: {user_id}")
            return True
            
        except Exception as e:
            self.db.rollback()
            logger.error(f"刪除用戶失敗: {str(e)}")
            raise e
    
    # 工具方法
    def _validate_unique_username(self, username: str):
        existing_user = self.db.query(User).filter(User.username == username).first()
        if existing_user:
            raise ValueError(f"用戶名已存在: {username}")
    
    def _validate_unique_email(self, email: str, exclude_id: int = None):
        query = self.db.query(User).filter(User.email == email)
        if exclude_id:
            query = query.filter(User.id != exclude_id)
        
        existing_user = query.first()
        if existing_user:
            raise ValueError(f"郵箱已存在: {email}")
    
    def _to_dict(self, user: User) -> dict:
        return user.to_dict()
    
    def __del__(self):
        if hasattr(self, 'db'):
            self.db.close()
```

### 5.7 小結

- **CREATE**：建立新資料，注意驗證唯一性約束
- **READ**：查詢資料，支援單筆、批次、分頁、條件查詢
- **UPDATE**：更新資料，確保資料完整性
- **DELETE**：刪除資料，考慮硬刪除或軟刪除

**實務建議：**

- 使用 DTO 模式分離內部模型和外部介面
- 實作適當的錯誤處理和日誌記錄
- 考慮軟刪除保留資料完整性
- 批次操作要注意效能和交易邊界

---

## 6. 關聯對映

### 6.1 關聯類型概述

```mermaid
graph TD
    A[關聯對映] --> B[One-to-One<br/>一對一]
    A --> C[One-to-Many<br/>一對多]
    A --> D[Many-to-Many<br/>多對多]
    
    B --> B1[單向關聯]
    B --> B2[雙向關聯]
    
    C --> C1[單向關聯]
    C --> C2[雙向關聯]
    
    D --> D1[聯結表]
    D --> D2[中間實體]
```

### 6.2 One-to-One (一對一關聯)

#### 6.2.1 Java 一對一關聯

```java
// User.java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(unique = true, nullable = false)
    private String username;
    
    // 一對一關聯：用戶檔案
    @OneToOne(mappedBy = "user", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private UserProfile profile;
    
    // 一對一關聯：用戶設定
    @OneToOne(cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    @JoinColumn(name = "user_settings_id")
    private UserSettings settings;
    
    // getter/setter...
}

// UserProfile.java
@Entity
@Table(name = "user_profiles")
public class UserProfile {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "first_name")
    private String firstName;
    
    @Column(name = "last_name")
    private String lastName;
    
    @Column(name = "phone_number")
    private String phoneNumber;
    
    @Lob
    private String bio;
    
    // 反向關聯
    @OneToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
    
    // getter/setter...
}

// UserSettings.java
@Entity
@Table(name = "user_settings")
public class UserSettings {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "email_notifications")
    private Boolean emailNotifications = true;
    
    @Column(name = "theme")
    private String theme = "light";
    
    @Column(name = "language")
    private String language = "zh-TW";
    
    // getter/setter...
}
```

#### 6.2.2 Python 一對一關聯

```python
# models.py
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    
    # 一對一關聯：用戶檔案
    profile = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    
    # 一對一關聯：用戶設定
    settings = relationship("UserSettings", uselist=False, cascade="all, delete-orphan")

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone_number = Column(String(20))
    bio = Column(Text)
    
    # 外鍵
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # 反向關聯
    user = relationship("User", back_populates="profile")

class UserSettings(Base):
    __tablename__ = 'user_settings'
    
    id = Column(Integer, primary_key=True)
    email_notifications = Column(Boolean, default=True)
    theme = Column(String(20), default='light')
    language = Column(String(10), default='zh-TW')
    
    # 外鍵
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # 關聯
    user = relationship("User", back_populates="settings")
```

### 6.3 One-to-Many (一對多關聯)

#### 6.3.1 Java 一對多關聯

```java
// User.java
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String username;
    
    // 一對多：用戶的訂單
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Order> orders = new ArrayList<>();
    
    // 一對多：用戶的評論
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Comment> comments = new ArrayList<>();
    
    // 便利方法
    public void addOrder(Order order) {
        orders.add(order);
        order.setUser(this);
    }
    
    public void removeOrder(Order order) {
        orders.remove(order);
        order.setUser(null);
    }
    
    // getter/setter...
}

// Order.java
@Entity
@Table(name = "orders")
public class Order {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "order_number", unique = true)
    private String orderNumber;
    
    @Enumerated(EnumType.STRING)
    private OrderStatus status;
    
    @Column(name = "total_amount")
    private BigDecimal totalAmount;
    
    @CreationTimestamp
    @Column(name = "created_at")
    private LocalDateTime createdAt;
    
    // 多對一：訂單屬於一個用戶
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
    
    // 一對多：訂單項目
    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<OrderItem> orderItems = new ArrayList<>();
    
    // getter/setter...
}

// OrderItem.java
@Entity
@Table(name = "order_items")
public class OrderItem {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "product_name")
    private String productName;
    
    private Integer quantity;
    
    @Column(name = "unit_price")
    private BigDecimal unitPrice;
    
    // 多對一：訂單項目屬於一個訂單
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "order_id", nullable = false)
    private Order order;
    
    // getter/setter...
}
```

#### 6.3.2 Python 一對多關聯

```python
# models.py
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from decimal import Decimal
import enum

class OrderStatus(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    
    # 一對多：用戶的訂單
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    
    # 一對多：用戶的評論
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")
    
    def add_order(self, order):
        """添加訂單"""
        self.orders.append(order)
        order.user = self
    
    def remove_order(self, order):
        """移除訂單"""
        if order in self.orders:
            self.orders.remove(order)
            order.user = None

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    order_number = Column(String(50), unique=True)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    total_amount = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 外鍵
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # 關聯
    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    
    def add_item(self, item):
        """添加訂單項目"""
        self.order_items.append(item)
        item.order = self
    
    def calculate_total(self):
        """計算總金額"""
        total = sum(item.quantity * item.unit_price for item in self.order_items)
        self.total_amount = total
        return total

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    quantity = Column(Integer)
    unit_price = Column(Numeric(10, 2))
    
    # 外鍵
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    
    # 關聯
    order = relationship("Order", back_populates="order_items")
    
    @property
    def subtotal(self):
        """計算小計"""
        return self.quantity * self.unit_price if self.quantity and self.unit_price else Decimal('0')
```

### 6.4 Many-to-Many (多對多關聯)

多對多關聯是最複雜的關聯類型，需要中間表來維護關係。典型的例子包括：學生與課程、書籍與作者、標籤與文章等。

#### 6.4.1 基本多對多關聯

**Java 範例 - 學生與課程：**

```java
@Entity
@Table(name = "students")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "student_name", nullable = false)
    private String name;
    
    @Column(name = "email", unique = true)
    private String email;
    
    // 多對多關聯：一個學生可以選修多門課程
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(
        name = "student_courses",                    // 中間表名稱
        joinColumns = @JoinColumn(name = "student_id"),        // 當前實體的外鍵
        inverseJoinColumns = @JoinColumn(name = "course_id")   // 關聯實體的外鍵
    )
    private Set<Course> courses = new HashSet<>();
    
    // 建構子、getter、setter
    public Student() {}
    
    public Student(String name, String email) {
        this.name = name;
        this.email = email;
    }
    
    // 便利方法：添加課程
    public void addCourse(Course course) {
        courses.add(course);
        course.getStudents().add(this);
    }
    
    // 便利方法：移除課程
    public void removeCourse(Course course) {
        courses.remove(course);
        course.getStudents().remove(this);
    }
    
    // getter 和 setter...
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    
    public Set<Course> getCourses() { return courses; }
    public void setCourses(Set<Course> courses) { this.courses = courses; }
}

@Entity
@Table(name = "courses")
public class Course {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "course_name", nullable = false)
    private String name;
    
    @Column(name = "course_code", unique = true)
    private String code;
    
    @Column(name = "credits")
    private Integer credits;
    
    // 多對多關聯的反向端
    @ManyToMany(mappedBy = "courses", fetch = FetchType.LAZY)
    private Set<Student> students = new HashSet<>();
    
    // 建構子、getter、setter
    public Course() {}
    
    public Course(String name, String code, Integer credits) {
        this.name = name;
        this.code = code;
        this.credits = credits;
    }
    
    // getter 和 setter...
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public String getCode() { return code; }
    public void setCode(String code) { this.code = code; }
    
    public Integer getCredits() { return credits; }
    public void setCredits(Integer credits) { this.credits = credits; }
    
    public Set<Student> getStudents() { return students; }
    public void setStudents(Set<Student> students) { this.students = students; }
}
```

**Python 範例 - 書籍與作者：**

```python
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 多對多關聯表
book_authors = Table(
    'book_authors', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True),
    Column('author_id', Integer, ForeignKey('authors.id'), primary_key=True)
)

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    isbn = Column(String(13), unique=True)
    publication_year = Column(Integer)
    
    # 多對多關聯：一本書可以有多個作者
    authors = relationship(
        "Author",
        secondary=book_authors,
        back_populates="books",
        lazy="select"  # 預設為延遲載入
    )
    
    def __init__(self, title, isbn=None, publication_year=None):
        self.title = title
        self.isbn = isbn
        self.publication_year = publication_year
    
    def add_author(self, author):
        """添加作者的便利方法"""
        if author not in self.authors:
            self.authors.append(author)
    
    def remove_author(self, author):
        """移除作者的便利方法"""
        if author in self.authors:
            self.authors.remove(author)
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}')>"

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(Integer)
    nationality = Column(String(50))
    
    # 多對多關聯的反向端
    books = relationship(
        "Book",
        secondary=book_authors,
        back_populates="authors",
        lazy="select"
    )
    
    def __init__(self, name, birth_year=None, nationality=None):
        self.name = name
        self.birth_year = birth_year
        self.nationality = nationality
    
    def add_book(self, book):
        """添加書籍的便利方法"""
        if book not in self.books:
            self.books.append(book)
            book.add_author(self)
    
    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"
```

#### 6.4.2 帶有額外屬性的多對多關聯

當中間表需要額外屬性時（如註冊時間、成績等），需要創建明確的中間實體：

**Java 範例 - 學生選課系統：**

```java
// 中間實體：學生選課記錄
@Entity
@Table(name = "student_course_enrollments")
public class Enrollment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "student_id")
    private Student student;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "course_id")
    private Course course;
    
    @Column(name = "enrollment_date")
    private LocalDate enrollmentDate;
    
    @Column(name = "grade")
    private String grade;  // A, B, C, D, F
    
    @Column(name = "semester")
    private String semester;
    
    // 建構子
    public Enrollment() {}
    
    public Enrollment(Student student, Course course, LocalDate enrollmentDate, String semester) {
        this.student = student;
        this.course = course;
        this.enrollmentDate = enrollmentDate;
        this.semester = semester;
    }
    
    // getter 和 setter...
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public Student getStudent() { return student; }
    public void setStudent(Student student) { this.student = student; }
    
    public Course getCourse() { return course; }
    public void setCourse(Course course) { this.course = course; }
    
    public LocalDate getEnrollmentDate() { return enrollmentDate; }
    public void setEnrollmentDate(LocalDate enrollmentDate) { this.enrollmentDate = enrollmentDate; }
    
    public String getGrade() { return grade; }
    public void setGrade(String grade) { this.grade = grade; }
    
    public String getSemester() { return semester; }
    public void setSemester(String semester) { this.semester = semester; }
}

// 更新 Student 實體
@Entity
@Table(name = "students")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String name;
    private String email;
    
    // 改為一對多關聯到中間實體
    @OneToMany(mappedBy = "student", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private Set<Enrollment> enrollments = new HashSet<>();
    
    // 便利方法：選課
    public void enrollInCourse(Course course, String semester) {
        Enrollment enrollment = new Enrollment(this, course, LocalDate.now(), semester);
        enrollments.add(enrollment);
        course.getEnrollments().add(enrollment);
    }
    
    // 便利方法：退課
    public void withdrawFromCourse(Course course) {
        enrollments.removeIf(enrollment -> enrollment.getCourse().equals(course));
        course.getEnrollments().removeIf(enrollment -> enrollment.getStudent().equals(this));
    }
    
    // getter 和 setter...
}

// 更新 Course 實體
@Entity
@Table(name = "courses")
public class Course {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String name;
    private String code;
    private Integer credits;
    
    @OneToMany(mappedBy = "course", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private Set<Enrollment> enrollments = new HashSet<>();
    
    // getter 和 setter...
}
```

**Python 範例 - 訂單商品系統：**

```python
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

class OrderItem(Base):
    """訂單商品中間實體"""
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    
    # 外鍵關聯
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    
    # 額外屬性
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Numeric(10, 2), nullable=False)
    discount_rate = Column(Numeric(5, 2), default=0)  # 折扣率
    
    # 關聯
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
    
    def __init__(self, order, product, quantity, unit_price, discount_rate=0):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.discount_rate = discount_rate
    
    @property
    def subtotal(self):
        """計算小計（含折扣）"""
        base_amount = self.quantity * self.unit_price
        discount_amount = base_amount * (self.discount_rate / 100)
        return base_amount - discount_amount

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    order_number = Column(String(50), unique=True, nullable=False)
    order_date = Column(DateTime, default=datetime.now)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    # 一對多關聯到中間實體
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    customer = relationship("Customer", back_populates="orders")
    
    def add_product(self, product, quantity, unit_price, discount_rate=0):
        """添加商品到訂單"""
        item = OrderItem(self, product, quantity, unit_price, discount_rate)
        self.items.append(item)
        return item
    
    @property
    def total_amount(self):
        """計算訂單總金額"""
        return sum(item.subtotal for item in self.items)

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    sku = Column(String(50), unique=True)
    price = Column(Numeric(10, 2), nullable=False)
    
    # 一對多關聯到中間實體
    order_items = relationship("OrderItem", back_populates="product")
```

#### 6.4.3 多對多關聯的最佳實務

**1. 使用 Set 而非 List**
```java
// ✅ 推薦：使用 Set 避免重複
@ManyToMany
private Set<Course> courses = new HashSet<>();

// ❌ 避免：List 可能導致重複和效能問題
@ManyToMany
private List<Course> courses = new ArrayList<>();
```

**2. 提供便利方法維護雙向關聯**
```java
public void addCourse(Course course) {
    courses.add(course);
    course.getStudents().add(this);
}

public void removeCourse(Course course) {
    courses.remove(course);
    course.getStudents().remove(this);
}
```

**3. 適當設定 Fetch 策略**
```java
// 預設使用 LAZY
@ManyToMany(fetch = FetchType.LAZY)
private Set<Course> courses = new HashSet<>();

// 需要時使用 EntityGraph 載入
@EntityGraph(attributePaths = {"courses"})
Student findByIdWithCourses(Long id);
```

**4. 考慮使用中間實體**
當需要額外屬性或複雜業務邏輯時，使用明確的中間實體更清晰。

#### 6.4.4 多對多查詢範例

**Java 查詢範例：**
```java
@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
    
    // 查找選修特定課程的所有學生
    @Query("SELECT s FROM Student s JOIN s.courses c WHERE c.code = :courseCode")
    List<Student> findStudentsByCourseCode(@Param("courseCode") String courseCode);
    
    // 查找選修課程數量超過指定數量的學生
    @Query("SELECT s FROM Student s WHERE SIZE(s.courses) > :minCourses")
    List<Student> findStudentsWithManyCourses(@Param("minCourses") int minCourses);
    
    // 使用 EntityGraph 載入學生和課程
    @EntityGraph(attributePaths = {"courses"})
    @Query("SELECT s FROM Student s WHERE s.id = :id")
    Optional<Student> findByIdWithCourses(@Param("id") Long id);
}
```

**Python 查詢範例：**
```python
from sqlalchemy.orm import selectinload

# 查找特定作者的所有書籍
def find_books_by_author(session, author_name):
    return session.query(Book).join(Book.authors).filter(
        Author.name == author_name
    ).all()

# 查找有多個作者的書籍
def find_books_with_multiple_authors(session):
    return session.query(Book).join(Book.authors).group_by(Book.id).having(
        func.count(Author.id) > 1
    ).all()

# 使用 selectinload 預載關聯資料
def find_author_with_books(session, author_id):
    return session.query(Author).options(
        selectinload(Author.books)
    ).filter(Author.id == author_id).first()

# 查找在特定年份出版且有特定作者的書籍
def find_books_by_year_and_author(session, year, author_name):
    return session.query(Book).join(Book.authors).filter(
        and_(
            Book.publication_year == year,
            Author.name.like(f"%{author_name}%")
        )
    ).all()
```

### 6.5 小結

- **一對一**：適用於擴展實體屬性或分離關注點，注意避免 N+1 問題
- **一對多**：最常見的關聯，注意 orphanRemoval 和 cascade 設定
- **多對多**：最複雜的關聯，需要中間表，當有額外屬性時考慮使用中間實體

**關聯對映最佳實務：**

- 優先使用 LAZY 載入，避免不必要的資料載入
- 適當設定 cascade 和 orphanRemoval 屬性
- 使用便利方法維護雙向關聯的一致性
- 多對多關聯使用 Set 而非 List，避免重複資料
- 複雜查詢時使用 EntityGraph 或 explicit loading 最佳化效能

**載入策略選擇指南：**

```mermaid
graph TD
    A[關聯資料載入] --> B{是否總是需要？}
    B -->|是| C[EAGER 載入]
    B -->|否| D[LAZY 載入]
    D --> E{是否批次操作？}
    E -->|是| F[使用 JOIN FETCH 或 EntityGraph]
    E -->|否| G[保持 LAZY，按需載入]
    
    C --> H[注意：可能導致過多資料載入]
    F --> I[注意：避免 N+1 問題]
    G --> J[注意：Session 必須保持開啟]
```

---

## 7. 進階主題

### 7.1 N+1 問題與解決方案

#### 7.1.1 什麼是 N+1 問題

```mermaid
sequenceDiagram
    participant App as 應用程式
    participant ORM as ORM 框架
    participant DB as 資料庫
    
    App->>ORM: 查詢所有用戶
    ORM->>DB: SELECT * FROM users (1 query)
    DB-->>ORM: 返回 N 個用戶
    
    loop 對每個用戶
        App->>ORM: 取得用戶訂單
        ORM->>DB: SELECT * FROM orders WHERE user_id = ? (N queries)
        DB-->>ORM: 返回訂單資料
    end
    
    Note over App,DB: 總共執行 1 + N 次查詢
```

#### 7.1.2 Java 解決 N+1 問題

```java
// ❌ 產生 N+1 問題的程式碼
@Service
public class BadUserService {
    
    public List<UserOrderSummary> getUserOrderSummaries() {
        List<User> users = userRepository.findAll(); // 1 query
        
        return users.stream()
            .map(user -> new UserOrderSummary(
                user.getId(),
                user.getUsername(),
                user.getOrders().size(), // N queries - 每個用戶一次查詢
                calculateTotalAmount(user.getOrders()) // 觸發載入
            ))
            .collect(Collectors.toList());
    }
}

// ✅ 解決方案 1: 使用 JOIN FETCH
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    @Query("SELECT DISTINCT u FROM User u LEFT JOIN FETCH u.orders")
    List<User> findAllWithOrders();
}

// ✅ 解決方案 2: 使用 EntityGraph
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    @EntityGraph(attributePaths = {"orders", "orders.orderItems"})
    List<User> findAllWithOrdersAndItems();
}

// ✅ 解決方案 3: 使用批次載入
@Entity
public class User {
    
    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY)
    @BatchSize(size = 10) // 批次載入，一次載入 10 個用戶的訂單
    private List<Order> orders;
}

// ✅ 解決方案 4: 使用投影查詢
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    @Query("SELECT new com.example.UserOrderSummary(u.id, u.username, COUNT(o), COALESCE(SUM(o.totalAmount), 0)) " +
           "FROM User u LEFT JOIN u.orders o " +
           "GROUP BY u.id, u.username")
    List<UserOrderSummary> findUserOrderSummaries();
}

// ✅ 最佳化的服務實作
@Service
public class OptimizedUserService {
    
    public List<UserOrderSummary> getUserOrderSummaries() {
        // 直接使用聚合查詢，避免 N+1 問題
        return userRepository.findUserOrderSummaries();
    }
    
    public List<User> getUsersWithOrders() {
        // 使用 EntityGraph 一次載入所有關聯資料
        return userRepository.findAllWithOrders();
    }
}
```

#### 7.1.3 Python 解決 N+1 問題

```python
# ❌ 產生 N+1 問題的程式碼
def get_user_order_summaries_bad():
    users = session.query(User).all()  # 1 query
    summaries = []
    
    for user in users:  # N queries
        order_count = len(user.orders)  # 觸發載入
        total_amount = sum(order.total_amount for order in user.orders)
        summaries.append({
            'user_id': user.id,
            'username': user.username,
            'order_count': order_count,
            'total_amount': total_amount
        })
    
    return summaries

# ✅ 解決方案 1: 使用 joinedload
from sqlalchemy.orm import joinedload

def get_users_with_orders_joined():
    return (session.query(User)
            .options(joinedload(User.orders))
            .all())

# ✅ 解決方案 2: 使用 selectinload (推薦用於一對多關聯)
from sqlalchemy.orm import selectinload

def get_users_with_orders_selectin():
    return (session.query(User)
            .options(selectinload(User.orders))
            .all())

# ✅ 解決方案 3: 使用 subqueryload
from sqlalchemy.orm import subqueryload

def get_users_with_orders_subquery():
    return (session.query(User)
            .options(subqueryload(User.orders))
            .all())

# ✅ 解決方案 4: 使用聚合查詢
def get_user_order_summaries_optimized():
    from sqlalchemy import func
    
    result = (session.query(
        User.id,
        User.username,
        func.count(Order.id).label('order_count'),
        func.coalesce(func.sum(Order.total_amount), 0).label('total_amount')
    )
    .outerjoin(Order)
    .group_by(User.id, User.username)
    .all())
    
    return [
        {
            'user_id': row.id,
            'username': row.username,
            'order_count': row.order_count,
            'total_amount': float(row.total_amount)
        }
        for row in result
    ]

# ✅ 解決方案 5: 巢狀載入
def get_users_with_nested_data():
    return (session.query(User)
            .options(
                selectinload(User.orders).selectinload(Order.order_items),
                joinedload(User.profile)
            )
            .all())

# 載入策略比較
class LoadingStrategyComparison:
    
    def compare_loading_strategies(self):
        """比較不同載入策略的效能"""
        import time
        
        strategies = {
            'lazy': self.lazy_loading,
            'joined': self.joined_loading,
            'selectin': self.selectin_loading,
            'subquery': self.subquery_loading
        }
        
        results = {}
        
        for name, strategy in strategies.items():
            start_time = time.time()
            
            # 清除 session 確保公平比較
            session.expunge_all()
            
            users = strategy()
            
            # 觸發載入以測量實際效能
            for user in users:
                _ = len(user.orders)
            
            end_time = time.time()
            results[name] = end_time - start_time
            
            print(f"{name}: {results[name]:.4f} seconds")
        
        return results
    
    def lazy_loading(self):
        return session.query(User).all()
    
    def joined_loading(self):
        return session.query(User).options(joinedload(User.orders)).all()
    
    def selectin_loading(self):
        return session.query(User).options(selectinload(User.orders)).all()
    
    def subquery_loading(self):
        return session.query(User).options(subqueryload(User.orders)).all()
```

### 7.2 快取策略

#### 7.2.1 多層快取架構

```mermaid
graph TD
    A[應用程式] --> B[應用層快取<br/>Redis/Memcached]
    B --> C[ORM 二級快取<br/>Hibernate/SQLAlchemy]
    C --> D[資料庫快取<br/>Query Cache]
    D --> E[磁碟儲存]
    
    F[快取策略] --> F1[Cache-Aside]
    F --> F2[Write-Through]
    F --> F3[Write-Behind]
    F --> F4[Refresh-Ahead]
```

#### 7.2.2 Java 快取實作

```java
// 使用 Spring Cache 的多層快取
@Configuration
@EnableCaching
public class CacheConfig {
    
    @Bean
    public CacheManager cacheManager() {
        RedisCacheManager.Builder builder = RedisCacheManager
            .RedisCacheManagerBuilder
            .fromConnectionFactory(redisConnectionFactory())
            .cacheDefaults(cacheConfiguration());
        
        return builder.build();
    }
    
    private RedisCacheConfiguration cacheConfiguration() {
        return RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(30))
            .serializeKeysWith(RedisSerializationContext.SerializationPair
                .fromSerializer(new StringRedisSerializer()))
            .serializeValuesWith(RedisSerializationContext.SerializationPair
                .fromSerializer(new GenericJackson2JsonRedisSerializer()));
    }
}

@Service
public class UserCacheService {
    
    @Cacheable(value = "users", key = "#id")
    public User findById(Long id) {
        return userRepository.findById(id).orElse(null);
    }
    
    @Cacheable(value = "userProfiles", key = "#userId")
    public UserProfile findUserProfile(Long userId) {
        return userProfileRepository.findByUserId(userId);
    }
    
    @CacheEvict(value = {"users", "userProfiles"}, key = "#user.id")
    public User updateUser(User user) {
        return userRepository.save(user);
    }
    
    @CacheEvict(value = "users", allEntries = true)
    public void clearAllUserCache() {
        // 清除所有用戶快取
    }
    
    // 條件快取
    @Cacheable(value = "expensiveCalculations", key = "#userId", 
               condition = "#userId > 100", unless = "#result == null")
    public UserStatistics calculateUserStatistics(Long userId) {
        // 昂貴的計算操作
        return performExpensiveCalculation(userId);
    }
    
    // 手動快取管理
    @Autowired
    private CacheManager cacheManager;
    
    public void evictUserCache(Long userId) {
        Cache userCache = cacheManager.getCache("users");
        if (userCache != null) {
            userCache.evict(userId);
        }
    }
    
    public User getCachedUser(Long userId) {
        Cache userCache = cacheManager.getCache("users");
        if (userCache != null) {
            Cache.ValueWrapper wrapper = userCache.get(userId);
            if (wrapper != null) {
                return (User) wrapper.get();
            }
        }
        return null;
    }
}

// 自定義快取註解
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@Cacheable(value = "userOperations")
public @interface UserCache {
    String key() default "";
    int expireAfterWrite() default 3600; // 秒
}

@Component
public class CacheableUserService {
    
    @UserCache(key = "#userId", expireAfterWrite = 1800)
    public UserDto getUserWithOrders(Long userId) {
        // 複雜的用戶資料組裝
        return assembleUserData(userId);
    }
}
```

#### 7.2.3 Python 快取實作

```python
# 使用 Redis 的快取裝飾器
import redis
import json
import functools
from typing import Optional, Any

class CacheManager:
    def __init__(self, redis_url: str = "redis://localhost:6379/0"):
        self.redis_client = redis.from_url(redis_url)
        self.default_timeout = 3600  # 1 小時
    
    def cache_key(self, prefix: str, *args, **kwargs) -> str:
        """生成快取鍵"""
        key_parts = [prefix] + [str(arg) for arg in args]
        if kwargs:
            key_parts.extend([f"{k}:{v}" for k, v in sorted(kwargs.items())])
        return ":".join(key_parts)
    
    def get(self, key: str) -> Optional[Any]:
        """從快取獲取資料"""
        try:
            value = self.redis_client.get(key)
            return json.loads(value) if value else None
        except (redis.RedisError, json.JSONDecodeError):
            return None
    
    def set(self, key: str, value: Any, timeout: Optional[int] = None) -> bool:
        """設定快取"""
        try:
            timeout = timeout or self.default_timeout
            return self.redis_client.setex(
                key, 
                timeout, 
                json.dumps(value, default=str)
            )
        except (redis.RedisError, json.JSONEncodeError):
            return False
    
    def delete(self, key: str) -> bool:
        """刪除快取"""
        try:
            return bool(self.redis_client.delete(key))
        except redis.RedisError:
            return False
    
    def cache_decorator(self, prefix: str, timeout: Optional[int] = None):
        """快取裝飾器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 生成快取鍵
                cache_key = self.cache_key(
                    f"{prefix}:{func.__name__}", 
                    *args, 
                    **kwargs
                )
                
                # 嘗試從快取獲取
                cached_result = self.get(cache_key)
                if cached_result is not None:
                    return cached_result
                
                # 執行函數並快取結果
                result = func(*args, **kwargs)
                if result is not None:
                    self.set(cache_key, result, timeout)
                
                return result
            return wrapper
        return decorator

# 全域快取管理器
cache_manager = CacheManager()

class CachedUserService:
    def __init__(self):
        self.db = SessionLocal()
    
    @cache_manager.cache_decorator("user", timeout=1800)
    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        """快取用戶查詢"""
        user = self.db.query(User).filter(User.id == user_id).first()
        return user.to_dict() if user else None
    
    @cache_manager.cache_decorator("user_stats", timeout=3600)
    def get_user_statistics(self, user_id: int) -> Optional[dict]:
        """快取用戶統計資料"""
        # 複雜的統計計算
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        
        stats = {
            'user_id': user_id,
            'order_count': len(user.orders),
            'total_spent': sum(order.total_amount for order in user.orders),
            'avg_order_value': 0,
            'last_order_date': None
        }
        
        if stats['order_count'] > 0:
            stats['avg_order_value'] = stats['total_spent'] / stats['order_count']
            stats['last_order_date'] = max(order.created_at for order in user.orders)
        
        return stats
    
    def update_user(self, user_id: int, **kwargs) -> Optional[dict]:
        """更新用戶並清除相關快取"""
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        
        # 更新用戶資料
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        self.db.commit()
        self.db.refresh(user)
        
        # 清除相關快取
        self._evict_user_cache(user_id)
        
        return user.to_dict()
    
    def _evict_user_cache(self, user_id: int):
        """清除用戶相關快取"""
        cache_patterns = [
            f"user:get_user_by_id:{user_id}",
            f"user_stats:get_user_statistics:{user_id}"
        ]
        
        for pattern in cache_patterns:
            cache_manager.delete(pattern)

# 快取預熱策略
class CacheWarmupService:
    def __init__(self):
        self.user_service = CachedUserService()
    
    def warmup_active_users(self):
        """預熱活躍用戶快取"""
        # 查詢最近活躍的用戶
        active_users = (self.user_service.db.query(User.id)
                       .filter(User.status == UserStatus.ACTIVE)
                       .limit(100)
                       .all())
        
        for user in active_users:
            # 預載入用戶資料和統計
            self.user_service.get_user_by_id(user.id)
            self.user_service.get_user_statistics(user.id)
        
        print(f"預熱了 {len(active_users)} 個用戶的快取")
    
    def warmup_popular_data(self):
        """預熱熱門資料"""
        # 這裡可以根據業務需求預載入常用資料
        pass
```

### 7.3 效能監控與調校

#### 7.3.1 SQL 執行監控

```java
// Java SQL 監控配置
@Component
public class SqlLoggingInterceptor implements Interceptor {
    
    private static final Logger logger = LoggerFactory.getLogger(SqlLoggingInterceptor.class);
    
    @Override
    public boolean onLoad(Object entity, Serializable id, Object[] state, String[] propertyNames, Type[] types) {
        logger.debug("Loading entity: {} with id: {}", entity.getClass().getSimpleName(), id);
        return false;
    }
    
    @Override
    public void afterTransactionCompletion(Transaction tx) {
        if (tx.wasCommitted()) {
            logger.debug("Transaction committed successfully");
        } else {
            logger.warn("Transaction was rolled back");
        }
    }
}

// 查詢效能監控
@Component
public class QueryPerformanceMonitor {
    
    private static final Logger perfLogger = LoggerFactory.getLogger("PERFORMANCE");
    
    @EventListener
    public void handleHibernateStatistics(ApplicationReadyEvent event) {
        SessionFactory sessionFactory = entityManagerFactory.unwrap(SessionFactory.class);
        Statistics stats = sessionFactory.getStatistics();
        stats.setStatisticsEnabled(true);
        
        // 定期記錄統計資訊
        scheduleStatisticsLogging(stats);
    }
    
    private void scheduleStatisticsLogging(Statistics stats) {
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);
        
        executor.scheduleAtFixedRate(() -> {
            perfLogger.info("Hibernate Statistics: " +
                "Queries executed: {}, " +
                "Cache hit ratio: {}, " +
                "Average query time: {} ms",
                stats.getQueryExecutionCount(),
                stats.getQueryCacheHitCount() * 100.0 / Math.max(1, stats.getQueryExecutionCount()),
                stats.getQueryExecutionMaxTime());
            
            // 記錄慢查詢
            if (stats.getQueryExecutionMaxTime() > 1000) {
                perfLogger.warn("Slow query detected: {} ms", stats.getQueryExecutionMaxTime());
            }
            
        }, 0, 60, TimeUnit.SECONDS);
    }
}
```

#### 7.3.2 Python 效能監控

```python
# SQL 執行時間監控
import time
import logging
from sqlalchemy import event
from sqlalchemy.engine import Engine

# 設定效能日誌
perf_logger = logging.getLogger('performance')
perf_logger.setLevel(logging.INFO)

class QueryPerformanceMonitor:
    def __init__(self):
        self.query_stats = {}
        self.slow_query_threshold = 1.0  # 1 秒
    
    def setup_monitoring(self, engine):
        """設定 SQLAlchemy 引擎監控"""
        event.listen(engine, "before_cursor_execute", self.before_cursor_execute)
        event.listen(engine, "after_cursor_execute", self.after_cursor_execute)
    
    def before_cursor_execute(self, conn, cursor, statement, parameters, context, executemany):
        """查詢執行前"""
        context._query_start_time = time.time()
        context._query_statement = statement
    
    def after_cursor_execute(self, conn, cursor, statement, parameters, context, executemany):
        """查詢執行後"""
        if hasattr(context, '_query_start_time'):
            total = time.time() - context._query_start_time
            
            # 記錄查詢統計
            self._record_query_stats(statement, total)
            
            # 記錄慢查詢
            if total > self.slow_query_threshold:
                perf_logger.warning(
                    f"Slow query detected: {total:.3f}s\n"
                    f"SQL: {statement[:200]}..."
                )
            
            perf_logger.debug(f"Query executed in {total:.3f}s: {statement[:100]}...")
    
    def _record_query_stats(self, statement: str, execution_time: float):
        """記錄查詢統計"""
        # 簡化 SQL 語句用於統計
        query_type = statement.strip().split()[0].upper()
        
        if query_type not in self.query_stats:
            self.query_stats[query_type] = {
                'count': 0,
                'total_time': 0,
                'min_time': float('inf'),
                'max_time': 0
            }
        
        stats = self.query_stats[query_type]
        stats['count'] += 1
        stats['total_time'] += execution_time
        stats['min_time'] = min(stats['min_time'], execution_time)
        stats['max_time'] = max(stats['max_time'], execution_time)
    
    def get_performance_report(self) -> dict:
        """獲取效能報告"""
        report = {}
        
        for query_type, stats in self.query_stats.items():
            if stats['count'] > 0:
                report[query_type] = {
                    'count': stats['count'],
                    'total_time': round(stats['total_time'], 3),
                    'avg_time': round(stats['total_time'] / stats['count'], 3),
                    'min_time': round(stats['min_time'], 3),
                    'max_time': round(stats['max_time'], 3)
                }
        
        return report
    
    def reset_stats(self):
        """重置統計資料"""
        self.query_stats.clear()

# 使用監控器
monitor = QueryPerformanceMonitor()
monitor.setup_monitoring(engine)

# 查詢分析工具
class QueryAnalyzer:
    def __init__(self, session):
        self.session = session
    
    def analyze_query(self, query_func, *args, **kwargs):
        """分析查詢效能"""
        # 清除 session 快取確保從資料庫載入
        self.session.expunge_all()
        
        # 記錄開始時間
        start_time = time.time()
        
        # 執行查詢
        result = query_func(*args, **kwargs)
        
        # 強制載入所有資料
        if hasattr(result, '__iter__'):
            list(result)  # 觸發載入
        
        # 計算執行時間
        execution_time = time.time() - start_time
        
        return {
            'result': result,
            'execution_time': execution_time,
            'query_count': self._get_query_count()
        }
    
    def _get_query_count(self):
        """獲取 session 中的查詢次數（簡化實作）"""
        # 實際實作需要使用 SQLAlchemy 的統計功能
        return "N/A"
    
    def compare_strategies(self, strategies: dict):
        """比較不同查詢策略的效能"""
        results = {}
        
        for name, strategy in strategies.items():
            print(f"測試策略: {name}")
            
            # 重置 session
            self.session.rollback()
            
            # 分析效能
            analysis = self.analyze_query(strategy)
            results[name] = analysis
            
            print(f"  執行時間: {analysis['execution_time']:.3f}s")
            print(f"  查詢次數: {analysis['query_count']}")
        
        return results

# 使用範例
def performance_test_example():
    analyzer = QueryAnalyzer(session)
    
    strategies = {
        'lazy_loading': lambda: session.query(User).all(),
        'eager_loading': lambda: session.query(User).options(selectinload(User.orders)).all(),
        'joined_loading': lambda: session.query(User).options(joinedload(User.orders)).all()
    }
    
    results = analyzer.compare_strategies(strategies)
    
    # 輸出比較結果
    best_strategy = min(results.items(), key=lambda x: x[1]['execution_time'])
    print(f"\n最佳策略: {best_strategy[0]} ({best_strategy[1]['execution_time']:.3f}s)")
```

### 7.4 小結

- **N+1 問題**：使用適當的載入策略（JOIN FETCH、EntityGraph、selectinload）
- **快取機制**：多層快取架構，合理設定過期時間和淘汰策略
- **效能監控**：監控 SQL 執行時間，識別慢查詢和效能瓶頸

**實務建議：**

- 建立效能監控機制，定期檢查查詢效能
- 根據業務場景選擇合適的載入和快取策略
- 使用工具進行查詢分析和最佳化
- 定期清理和更新快取資料

---

## 8. 專案最佳實務

### 8.1 命名規則

#### 8.1.1 實體和表格命名

```java
// ✅ 好的命名範例
@Entity
@Table(name = "users")  // 表格名稱使用複數、snake_case
public class User {     // 類別名稱使用單數、PascalCase
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "first_name")  // 欄位使用 snake_case
    private String firstName;     // 屬性使用 camelCase
    
    @Column(name = "email_address")
    private String emailAddress;
    
    @Column(name = "created_at")
    private LocalDateTime createdAt;
}

// ❌ 避免的命名方式
@Entity
@Table(name = "User")  // 避免：表格名稱不應使用大寫
public class user {    // 避免：類別名稱應該大寫開頭
    
    @Column(name = "FirstName")  // 避免：欄位名稱不應使用 PascalCase
    private String first_name;   // 避免：Java 屬性不應使用 snake_case
}
```

#### 8.1.2 Repository 和 Service 命名

```java
// Repository 命名規則
public interface UserRepository extends JpaRepository<User, Long> {
    // 查詢方法命名要清晰表達意圖
    Optional<User> findByEmail(String email);
    List<User> findByStatusAndCreatedAtAfter(UserStatus status, LocalDateTime date);
    
    // 使用 @Query 時保持方法名稱與查詢意圖一致
    @Query("SELECT u FROM User u WHERE u.email LIKE %:domain%")
    List<User> findUsersByEmailDomain(@Param("domain") String domain);
}

// Service 命名規則
@Service
public class UserService {
    
    // 業務方法使用動詞開頭
    public User createUser(CreateUserRequest request);
    public User updateUserProfile(Long userId, UpdateProfileRequest request);
    public void deactivateUser(Long userId);
    
    // 查詢方法可以使用 find/get 開頭
    public UserDto findUserById(Long id);
    public List<UserDto> getActiveUsers();
    public Page<UserDto> searchUsers(UserSearchCriteria criteria, Pageable pageable);
}
```

### 8.2 錯誤處理

#### 8.2.1 Java 異常處理策略

```java
// 自定義異常類別
public class UserNotFoundException extends RuntimeException {
    private final Long userId;
    
    public UserNotFoundException(Long userId) {
        super(String.format("User with id %d not found", userId));
        this.userId = userId;
    }
    
    public Long getUserId() {
        return userId;
    }
}

public class UserValidationException extends RuntimeException {
    private final List<String> validationErrors;
    
    public UserValidationException(List<String> errors) {
        super("User validation failed: " + String.join(", ", errors));
        this.validationErrors = errors;
    }
    
    public List<String> getValidationErrors() {
        return validationErrors;
    }
}

// Service 層錯誤處理
@Service
@Transactional
public class UserService {
    
    private static final Logger logger = LoggerFactory.getLogger(UserService.class);
    
    public User createUser(CreateUserRequest request) {
        try {
            // 驗證請求
            validateCreateUserRequest(request);
            
            // 檢查用戶是否已存在
            if (userRepository.findByEmail(request.getEmail()).isPresent()) {
                throw new UserValidationException(
                    Arrays.asList("Email already exists: " + request.getEmail())
                );
            }
            
            User user = new User();
            user.setUsername(request.getUsername());
            user.setEmail(request.getEmail());
            
            User savedUser = userRepository.save(user);
            logger.info("User created successfully with id: {}", savedUser.getId());
            
            return savedUser;
            
        } catch (DataIntegrityViolationException e) {
            logger.error("Data integrity violation while creating user", e);
            throw new UserValidationException(
                Arrays.asList("User data violates database constraints")
            );
        } catch (Exception e) {
            logger.error("Unexpected error while creating user", e);
            throw new RuntimeException("Failed to create user", e);
        }
    }
    
    public User findUserById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
    
    private void validateCreateUserRequest(CreateUserRequest request) {
        List<String> errors = new ArrayList<>();
        
        if (StringUtils.isBlank(request.getUsername())) {
            errors.add("Username is required");
        }
        
        if (StringUtils.isBlank(request.getEmail())) {
            errors.add("Email is required");
        } else if (!EmailValidator.getInstance().isValid(request.getEmail())) {
            errors.add("Invalid email format");
        }
        
        if (!errors.isEmpty()) {
            throw new UserValidationException(errors);
        }
    }
}

// 全域異常處理器
@ControllerAdvice
public class GlobalExceptionHandler {
    
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException e) {
        logger.warn("User not found: {}", e.getMessage());
        
        ErrorResponse error = new ErrorResponse(
            "USER_NOT_FOUND",
            e.getMessage(),
            LocalDateTime.now()
        );
        
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(UserValidationException.class)
    public ResponseEntity<ErrorResponse> handleUserValidation(UserValidationException e) {
        logger.warn("User validation failed: {}", e.getMessage());
        
        ErrorResponse error = new ErrorResponse(
            "VALIDATION_ERROR",
            e.getMessage(),
            LocalDateTime.now()
        );
        error.setDetails(e.getValidationErrors());
        
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
    }
    
    @ExceptionHandler(DataIntegrityViolationException.class)
    public ResponseEntity<ErrorResponse> handleDataIntegrityViolation(DataIntegrityViolationException e) {
        logger.error("Data integrity violation", e);
        
        ErrorResponse error = new ErrorResponse(
            "DATA_INTEGRITY_ERROR",
            "Data violates database constraints",
            LocalDateTime.now()
        );
        
        return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
    }
}
```

#### 8.2.2 Python 異常處理策略

```python
# 自定義異常類別
class UserServiceException(Exception):
    """用戶服務基礎異常"""
    pass

class UserNotFoundException(UserServiceException):
    """用戶不存在異常"""
    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(f"User with id {user_id} not found")

class UserValidationException(UserServiceException):
    """用戶驗證異常"""
    def __init__(self, errors: list):
        self.errors = errors
        super().__init__(f"User validation failed: {', '.join(errors)}")

class DatabaseOperationException(UserServiceException):
    """資料庫操作異常"""
    pass

# Service 層錯誤處理
import logging
from typing import Optional, Dict, Any
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self):
        self.db = SessionLocal()
    
    def create_user(self, user_data: dict) -> dict:
        """建立用戶並處理各種異常"""
        try:
            # 驗證資料
            self._validate_user_data(user_data)
            
            # 檢查用戶是否已存在
            existing_user = (self.db.query(User)
                           .filter(User.email == user_data['email'])
                           .first())
            
            if existing_user:
                raise UserValidationException(['Email already exists'])
            
            # 建立用戶
            user = User(**user_data)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            
            logger.info(f"User created successfully with id: {user.id}")
            return user.to_dict()
            
        except UserValidationException:
            self.db.rollback()
            raise  # 重新拋出驗證異常
            
        except IntegrityError as e:
            self.db.rollback()
            logger.error(f"Database integrity error: {str(e)}")
            raise DatabaseOperationException("User data violates database constraints")
            
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Database error while creating user: {str(e)}")
            raise DatabaseOperationException("Database operation failed")
            
        except Exception as e:
            self.db.rollback()
            logger.error(f"Unexpected error while creating user: {str(e)}")
            raise UserServiceException("Failed to create user")
    
    def get_user_by_id(self, user_id: int) -> dict:
        """根據 ID 獲取用戶"""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundException(user_id)
            
            return user.to_dict()
            
        except UserNotFoundException:
            raise  # 重新拋出用戶不存在異常
            
        except SQLAlchemyError as e:
            logger.error(f"Database error while fetching user {user_id}: {str(e)}")
            raise DatabaseOperationException("Failed to fetch user")
    
    def _validate_user_data(self, user_data: dict):
        """驗證用戶資料"""
        errors = []
        
        if not user_data.get('username'):
            errors.append('Username is required')
        
        email = user_data.get('email')
        if not email:
            errors.append('Email is required')
        elif not self._is_valid_email(email):
            errors.append('Invalid email format')
        
        if errors:
            raise UserValidationException(errors)
    
    def _is_valid_email(self, email: str) -> bool:
        """簡單的郵箱驗證"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def __del__(self):
        if hasattr(self, 'db'):
            self.db.close()

# Flask 錯誤處理（如果使用 Flask）
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.errorhandler(UserNotFoundException)
def handle_user_not_found(e):
    logger.warning(f"User not found: {str(e)}")
    return jsonify({
        'error': 'USER_NOT_FOUND',
        'message': str(e),
        'user_id': e.user_id
    }), 404

@app.errorhandler(UserValidationException)
def handle_user_validation(e):
    logger.warning(f"User validation failed: {str(e)}")
    return jsonify({
        'error': 'VALIDATION_ERROR',
        'message': str(e),
        'details': e.errors
    }), 400

@app.errorhandler(DatabaseOperationException)
def handle_database_error(e):
    logger.error(f"Database operation failed: {str(e)}")
    return jsonify({
        'error': 'DATABASE_ERROR',
        'message': str(e)
    }), 500

@app.errorhandler(Exception)
def handle_unexpected_error(e):
    logger.error(f"Unexpected error: {str(e)}")
    return jsonify({
        'error': 'INTERNAL_ERROR',
        'message': 'An unexpected error occurred'
    }), 500
```

### 8.3 測試策略

#### 8.3.1 Java 測試實作

```java
// 單元測試
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void createUser_WithValidData_ShouldReturnUser() {
        // Given
        CreateUserRequest request = new CreateUserRequest("john_doe", "john@example.com");
        User savedUser = new User();
        savedUser.setId(1L);
        savedUser.setUsername("john_doe");
        savedUser.setEmail("john@example.com");
        
        when(userRepository.findByEmail(request.getEmail())).thenReturn(Optional.empty());
        when(userRepository.save(any(User.class))).thenReturn(savedUser);
        
        // When
        User result = userService.createUser(request);
        
        // Then
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo(1L);
        assertThat(result.getUsername()).isEqualTo("john_doe");
        verify(userRepository).findByEmail(request.getEmail());
        verify(userRepository).save(any(User.class));
    }
    
    @Test
    void createUser_WithExistingEmail_ShouldThrowException() {
        // Given
        CreateUserRequest request = new CreateUserRequest("john_doe", "john@example.com");
        User existingUser = new User();
        
        when(userRepository.findByEmail(request.getEmail())).thenReturn(Optional.of(existingUser));
        
        // When & Then
        assertThrows(UserValidationException.class, () -> userService.createUser(request));
        verify(userRepository, never()).save(any(User.class));
    }
}

// 整合測試
@SpringBootTest
@Transactional
@TestPropertySource(properties = {
    "spring.datasource.url=jdbc:h2:mem:testdb",
    "spring.jpa.hibernate.ddl-auto=create-drop"
})
class UserServiceIntegrationTest {
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void createUser_IntegrationTest() {
        // Given
        CreateUserRequest request = new CreateUserRequest("integration_user", "integration@example.com");
        
        // When
        User createdUser = userService.createUser(request);
        
        // Then
        assertThat(createdUser.getId()).isNotNull();
        
        Optional<User> foundUser = userRepository.findById(createdUser.getId());
        assertThat(foundUser).isPresent();
        assertThat(foundUser.get().getUsername()).isEqualTo("integration_user");
    }
    
    @Test
    void findUserById_WithNonExistentId_ShouldThrowException() {
        // When & Then
        assertThrows(UserNotFoundException.class, () -> userService.findUserById(999L));
    }
}

// Repository 測試
@DataJpaTest
class UserRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void findByEmail_WithExistingEmail_ShouldReturnUser() {
        // Given
        User user = new User();
        user.setUsername("test_user");
        user.setEmail("test@example.com");
        entityManager.persistAndFlush(user);
        
        // When
        Optional<User> found = userRepository.findByEmail("test@example.com");
        
        // Then
        assertThat(found).isPresent();
        assertThat(found.get().getUsername()).isEqualTo("test_user");
    }
    
    @Test
    void findByEmail_WithNonExistentEmail_ShouldReturnEmpty() {
        // When
        Optional<User> found = userRepository.findByEmail("nonexistent@example.com");
        
        // Then
        assertThat(found).isEmpty();
    }
}
```

#### 8.3.2 Python 測試實作

```python
# 測試配置
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, UserStatus

# 測試資料庫設定
TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def test_db():
    """測試資料庫 fixture"""
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(engine)
    
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestSessionLocal()
    
    yield session
    
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture
def sample_user():
    """範例用戶資料"""
    return {
        'username': 'test_user',
        'email': 'test@example.com',
        'full_name': 'Test User'
    }

# 單元測試
class TestUserService:
    
    def test_create_user_success(self, test_db, sample_user):
        """測試成功建立用戶"""
        # Arrange
        service = UserService()
        service.db = test_db
        
        # Act
        result = service.create_user(**sample_user)
        
        # Assert
        assert result['username'] == sample_user['username']
        assert result['email'] == sample_user['email']
        assert result['id'] is not None
        
        # 驗證資料庫中確實建立了用戶
        user_in_db = test_db.query(User).filter(User.email == sample_user['email']).first()
        assert user_in_db is not None
        assert user_in_db.username == sample_user['username']
    
    def test_create_user_duplicate_email(self, test_db, sample_user):
        """測試重複郵箱建立用戶應該失敗"""
        # Arrange
        service = UserService()
        service.db = test_db
        
        # 先建立一個用戶
        service.create_user(**sample_user)
        
        # Act & Assert
        with pytest.raises(ValueError, match="郵箱已存在"):
            service.create_user(**sample_user)
    
    def test_get_user_by_id_success(self, test_db, sample_user):
        """測試成功獲取用戶"""
        # Arrange
        service = UserService()
        service.db = test_db
        
        created_user = service.create_user(**sample_user)
        user_id = created_user['id']
        
        # Act
        result = service.get_user_by_id(user_id)
        
        # Assert
        assert result['id'] == user_id
        assert result['username'] == sample_user['username']
    
    def test_get_user_by_id_not_found(self, test_db):
        """測試獲取不存在的用戶"""
        # Arrange
        service = UserService()
        service.db = test_db
        
        # Act & Assert
        with pytest.raises(ValueError, match="用戶不存在: 999"):
            service.get_user_by_id(999)
    
    def test_update_user_success(self, test_db, sample_user):
        """測試成功更新用戶"""
        # Arrange
        service = UserService()
        service.db = test_db
        
        created_user = service.create_user(**sample_user)
        user_id = created_user['id']
        
        # Act
        updated_data = {
            'email': 'updated@example.com',
            'full_name': 'Updated Name'
        }
        result = service.update_user(user_id, **updated_data)
        
        # Assert
        assert result['email'] == updated_data['email']
        assert result['full_name'] == updated_data['full_name']
        assert result['username'] == sample_user['username']  # 未更新的欄位保持不變

# 整合測試
class TestUserServiceIntegration:
    
    def test_user_lifecycle(self, test_db):
        """測試用戶完整生命週期"""
        service = UserService()
        service.db = test_db
        
        # 建立用戶
        user_data = {
            'username': 'lifecycle_user',
            'email': 'lifecycle@example.com',
            'full_name': 'Lifecycle User'
        }
        
        created_user = service.create_user(**user_data)
        user_id = created_user['id']
        
        # 驗證建立
        assert created_user['username'] == user_data['username']
        
        # 更新用戶
        updated_user = service.update_user(user_id, full_name='Updated Lifecycle User')
        assert updated_user['full_name'] == 'Updated Lifecycle User'
        
        # 刪除用戶
        success = service.delete_user(user_id)
        assert success is True
        
        # 驗證刪除
        with pytest.raises(ValueError):
            service.get_user_by_id(user_id)

# 效能測試
class TestUserServicePerformance:
    
    def test_batch_create_performance(self, test_db):
        """測試批次建立用戶的效能"""
        import time
        
        service = UserService()
        service.db = test_db
        
        # 準備測試資料
        users_data = [
            {
                'username': f'user_{i}',
                'email': f'user_{i}@example.com',
                'full_name': f'User {i}'
            }
            for i in range(100)
        ]
        
        # 測試批次建立
        start_time = time.time()
        
        for user_data in users_data:
            service.create_user(**user_data)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # 驗證結果
        user_count = test_db.query(User).count()
        assert user_count == 100
        
        # 效能斷言（根據實際情況調整）
        assert execution_time < 5.0  # 應該在 5 秒內完成
        
        print(f"批次建立 100 個用戶耗時: {execution_time:.2f} 秒")

# 執行測試的指令範例
if __name__ == "__main__":
    # pytest test_user_service.py -v
    # pytest test_user_service.py::TestUserService::test_create_user_success -v
    # pytest test_user_service.py --cov=user_service --cov-report=html
    pass
```

### 8.4 小結

- **命名規則**：一致的命名約定提高程式碼可讀性
- **錯誤處理**：分層的異常處理策略和適當的日誌記錄
- **測試策略**：單元測試、整合測試和效能測試的完整覆蓋

**實務建議：**

- 建立團隊程式碼規範並嚴格執行
- 使用自動化工具檢查程式碼品質
- 編寫全面的測試覆蓋關鍵業務邏輯
- 定期進行程式碼審查和重構

---

## 9. 常見錯誤與排錯技巧

### 9.1 LazyInitializationException

#### 9.1.1 問題描述

```java
// ❌ 常見錯誤：在 Session 關閉後存取延遲載入的屬性
@Service
public class UserService {
    
    @Transactional
    public User findUser(Long id) {
        return userRepository.findById(id).orElse(null);
    }
    
    // 問題：在方法外存取 orders 會拋出 LazyInitializationException
    public void processUserOrders(Long userId) {
        User user = findUser(userId); // Transaction 結束，Session 關閉
        List<Order> orders = user.getOrders(); // ❌ LazyInitializationException
    }
}
```

#### 9.1.2 解決方案

```java
// ✅ 解決方案 1: 在 Transaction 內完成所有操作
@Service
public class UserService {
    
    @Transactional
    public void processUserOrders(Long userId) {
        User user = userRepository.findById(userId).orElse(null);
        if (user != null) {
            List<Order> orders = user.getOrders(); // ✅ 在 Transaction 內存取
            // 處理訂單邏輯
        }
    }
}

// ✅ 解決方案 2: 使用 EAGER 載入
@Entity
public class User {
    @OneToMany(mappedBy = "user", fetch = FetchType.EAGER)
    private List<Order> orders;
}

// ✅ 解決方案 3: 使用 JOIN FETCH
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    @Query("SELECT u FROM User u LEFT JOIN FETCH u.orders WHERE u.id = :id")
    Optional<User> findByIdWithOrders(@Param("id") Long id);
}

// ✅ 解決方案 4: 使用 EntityGraph
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    @EntityGraph(attributePaths = {"orders"})
    Optional<User> findById(Long id);
}

// ✅ 解決方案 5: 使用 DTO 模式
@Service
public class UserService {
    
    @Transactional(readOnly = true)
    public UserWithOrdersDto findUserWithOrders(Long userId) {
        User user = userRepository.findById(userId).orElse(null);
        if (user == null) {
            return null;
        }
        
        // 在 Transaction 內轉換為 DTO
        return new UserWithOrdersDto(
            user.getId(),
            user.getUsername(),
            user.getOrders().stream()
                .map(this::convertToOrderDto)
                .collect(Collectors.toList())
        );
    }
}
```

#### 9.1.3 Python 類似問題

```python
# ❌ 常見錯誤：Session 關閉後存取關聯資料
def get_user_orders_bad(user_id):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    finally:
        session.close()

# 在外部存取會出錯
user = get_user_orders_bad(1)
orders = user.orders  # ❌ DetachedInstanceError

# ✅ 解決方案 1: 在 Session 內完成操作
def get_user_orders_good(user_id):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            # 強制載入關聯資料
            orders = user.orders
            return {
                'user_id': user.id,
                'username': user.username,
                'orders': [order.to_dict() for order in orders]
            }
        return None
    finally:
        session.close()

# ✅ 解決方案 2: 使用 eager loading
def get_user_with_orders_eager(user_id):
    session = SessionLocal()
    try:
        user = (session.query(User)
                .options(selectinload(User.orders))
                .filter(User.id == user_id)
                .first())
        return user
    finally:
        session.close()
```

### 9.2 N+1 查詢問題

#### 9.2.1 識別 N+1 問題

```java
// 啟用 SQL 日誌來識別 N+1 問題
# application.yml
logging:
  level:
    org.hibernate.SQL: DEBUG
    org.hibernate.type.descriptor.sql.BasicBinder: TRACE

spring:
  jpa:
    show-sql: true
    properties:
      hibernate:
        format_sql: true
        generate_statistics: true
```

```python
# Python 中識別 N+1 問題
import logging

# 啟用 SQL 日誌
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# 使用查詢計數器
class QueryCounter:
    def __init__(self):
        self.query_count = 0
    
    def count_queries(self, conn, cursor, statement, parameters, context, executemany):
        self.query_count += 1
        print(f"Query #{self.query_count}: {statement[:100]}...")

# 監控查詢次數
from sqlalchemy import event
counter = QueryCounter()
event.listen(engine, "before_cursor_execute", counter.count_queries)
```

### 9.3 資料庫連線問題

#### 9.3.1 連線池設定

```java
// Java 連線池最佳化
spring:
  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      idle-timeout: 300000
      connection-timeout: 20000
      leak-detection-threshold: 60000
      max-lifetime: 1800000
```

```python
# Python 連線池設定
from sqlalchemy import create_engine

engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # 基本連線數
    max_overflow=20,       # 最大溢出連線
    pool_pre_ping=True,    # 連線檢查
    pool_recycle=3600,     # 連線回收時間（秒）
    echo=False             # 生產環境關閉 SQL 日誌
)
```

### 9.4 效能問題排錯

#### 9.4.1 慢查詢識別

```java
// Java 慢查詢監控
@Component
public class SlowQueryLogger {
    
    private static final Logger logger = LoggerFactory.getLogger("SLOW_QUERY");
    
    @EventListener
    public void handleSlowQuery(StatementInspector.SlowQueryEvent event) {
        if (event.getExecutionTime() > 1000) { // 超過 1 秒
            logger.warn("Slow query detected: {} ms\nSQL: {}", 
                       event.getExecutionTime(), 
                       event.getSql());
        }
    }
}
```

```python
# Python 慢查詢監控
import time
from sqlalchemy import event

class SlowQueryLogger:
    def __init__(self, threshold_ms=1000):
        self.threshold_ms = threshold_ms
    
    def before_cursor_execute(self, conn, cursor, statement, parameters, context, executemany):
        context._query_start_time = time.time()
    
    def after_cursor_execute(self, conn, cursor, statement, parameters, context, executemany):
        if hasattr(context, '_query_start_time'):
            total = time.time() - context._query_start_time
            if total * 1000 > self.threshold_ms:
                print(f"SLOW QUERY: {total*1000:.2f}ms\n{statement[:200]}...")

# 註冊監聽器
slow_query_logger = SlowQueryLogger()
event.listen(engine, "before_cursor_execute", slow_query_logger.before_cursor_execute)
event.listen(engine, "after_cursor_execute", slow_query_logger.after_cursor_execute)
```

### 9.5 資料一致性問題

#### 9.5.1 交易隔離等級

```java
// Java 交易隔離等級設定
@Transactional(isolation = Isolation.READ_COMMITTED)
public void updateUserBalance(Long userId, BigDecimal amount) {
    // 防止髒讀，但允許不可重複讀
}

@Transactional(isolation = Isolation.REPEATABLE_READ)
public void generateReport(Long userId) {
    // 防止髒讀和不可重複讀
}
```

```python
# Python 交易隔離等級
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 設定隔離等級
engine = create_engine(DATABASE_URL, isolation_level="READ_COMMITTED")

# 或在 session 層級設定
def with_isolation_level(isolation_level):
    connection = engine.connect()
    trans = connection.begin()
    try:
        connection.execute(f"SET TRANSACTION ISOLATION LEVEL {isolation_level}")
        session = sessionmaker(bind=connection)()
        yield session
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        connection.close()
```

### 9.6 記憶體洩漏問題

#### 9.6.1 Session 管理

```java
// ❌ 錯誤：沒有正確關閉 EntityManager
@Service
public class BadUserService {
    
    @PersistenceContext
    private EntityManager entityManager;
    
    public void processLargeDataset() {
        for (int i = 0; i < 10000; i++) {
            User user = new User();
            entityManager.persist(user);
            // ❌ 沒有 flush 和 clear，導致一級快取堆積
        }
    }
}

// ✅ 正確：定期清理一級快取
@Service
public class GoodUserService {
    
    @PersistenceContext
    private EntityManager entityManager;
    
    @Transactional
    public void processLargeDataset() {
        int batchSize = 50;
        
        for (int i = 0; i < 10000; i++) {
            User user = new User();
            entityManager.persist(user);
            
            if (i % batchSize == 0) {
                entityManager.flush();  // 強制執行 SQL
                entityManager.clear();  // 清除一級快取
            }
        }
    }
}
```

### 9.7 常見錯誤檢查清單

#### 9.7.1 開發階段檢查

```mermaid
graph TD
    A[開發階段檢查] --> B[實體設計]
    A --> C[關聯配置]
    A --> D[查詢效能]
    A --> E[交易管理]
    
    B --> B1[✓ 主鍵策略正確]
    B --> B2[✓ 欄位對映正確]
    B --> B3[✓ 索引設定適當]
    
    C --> C1[✓ Fetch 策略合理]
    C --> C2[✓ Cascade 設定正確]
    C --> C3[✓ 避免循環引用]
    
    D --> D1[✓ 避免 N+1 問題]
    D --> D2[✓ 使用適當的載入策略]
    D --> D3[✓ 查詢結果有限制]
    
    E --> E1[✓ 交易邊界明確]
    E --> E2[✓ 異常處理完整]
    E --> E3[✓ 資源正確釋放]
```

#### 9.7.2 生產環境檢查

| 檢查項目 | 檢查內容 | 解決方案 |
|----------|----------|----------|
| 慢查詢 | 執行時間 > 1秒的查詢 | 添加索引、優化查詢 |
| 記憶體使用 | JVM/Python 進程記憶體 | 調整快取設定、批次處理 |
| 連線數 | 資料庫連線池使用率 | 調整連線池大小 |
| 錯誤率 | 異常發生頻率 | 完善錯誤處理 |
| 響應時間 | API 平均響應時間 | 查詢最佳化、快取策略 |

### 9.8 小結

- **LazyInitializationException**：確保在 Transaction 內存取關聯資料
- **N+1 問題**：使用適當的載入策略和查詢最佳化
- **效能問題**：監控慢查詢，合理設定快取和連線池
- **記憶體洩漏**：定期清理 Session 快取，適當管理資源

**排錯建議：**

- 啟用詳細的 SQL 日誌以識別問題
- 使用效能監控工具追蹤關鍵指標
- 建立完善的異常處理和日誌記錄
- 定期進行效能測試和程式碼審查

---

## 10. 認證考試重點與練習題

### 10.1 Java JPA/Hibernate 認證重點

#### 10.1.1 核心概念 (20%)

**重點知識:**
- JPA 規範與 Hibernate 實作的關係
- EntityManager 和 Session 的生命週期
- 持久化上下文 (Persistence Context) 的概念
- 實體狀態：Transient、Persistent、Detached、Removed

**練習題:**

```java
// 題目 1: 以下程式碼會輸出什麼？
@Entity
public class Product {
    @Id
    @GeneratedValue
    private Long id;
    private String name;
    // getter/setter...
}

@Service
public class ProductService {
    @PersistenceContext
    private EntityManager em;
    
    @Transactional
    public void testEntityStates() {
        Product p1 = new Product();  // 狀態: ?
        p1.setName("Laptop");
        
        em.persist(p1);             // 狀態: ?
        System.out.println("ID after persist: " + p1.getId());
        
        em.flush();                 // 狀態: ?
        System.out.println("ID after flush: " + p1.getId());
        
        em.detach(p1);             // 狀態: ?
        p1.setName("Desktop");
        
        em.merge(p1);              // 狀態: ?
    }
}
```

**答案:**
1. Transient（瞬時）
2. Persistent（持久），ID 仍為 null
3. Persistent，ID 已生成
4. Detached（分離）
5. 返回新的 Persistent 實體

#### 10.1.2 實體對映 (25%)

**重點知識:**
- 基本註解：@Entity、@Table、@Column、@Id
- 主鍵生成策略：GenerationType 的各種選項
- 時間日期對映：@Temporal、LocalDateTime
- 大型物件對映：@Lob
- 列舉型別對映：@Enumerated

**練習題:**

```java
// 題目 2: 修正以下實體類別的對映錯誤
@Entity
@Table(name = "employees")
public class Employee {
    @Id
    private String id;  // 錯誤 1: 缺少生成策略
    
    @Column(name = "emp_name")
    private String employeeName;
    
    private Date birthDate;  // 錯誤 2: 缺少時間精度
    
    @Enumerated
    private Status status;   // 錯誤 3: 缺少列舉策略
    
    private byte[] photo;    // 錯誤 4: 大型物件未標註
}

enum Status {
    ACTIVE, INACTIVE, SUSPENDED
}
```

**答案:**
```java
@Entity
@Table(name = "employees")
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)  // 修正 1
    private Long id;  // 改為 Long 類型
    
    @Column(name = "emp_name", nullable = false, length = 100)
    private String employeeName;
    
    @Temporal(TemporalType.DATE)  // 修正 2
    private Date birthDate;
    
    @Enumerated(EnumType.STRING)  // 修正 3
    private Status status;
    
    @Lob  // 修正 4
    private byte[] photo;
}
```

#### 10.1.3 關聯對映 (30%)

**重點知識:**
- 一對一：@OneToOne、@JoinColumn
- 一對多/多對一：@OneToMany、@ManyToOne、mappedBy
- 多對多：@ManyToMany、@JoinTable
- 級聯操作：CascadeType 選項
- Fetch 策略：FetchType.LAZY vs EAGER

**練習題:**

```java
// 題目 3: 設計一個部落格系統的實體關聯
// 需求：
// - 用戶可以寫多篇文章
// - 文章可以有多個標籤
// - 文章可以有多個評論
// - 評論屬於特定文章和用戶

// 請完成以下實體類別：

@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    
    // TODO: 添加與 Post 的關聯
    // TODO: 添加與 Comment 的關聯
}

@Entity
public class Post {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String content;
    
    // TODO: 添加與 User 的關聯
    // TODO: 添加與 Tag 的關聯
    // TODO: 添加與 Comment 的關聯
}

@Entity
public class Tag {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    
    // TODO: 添加與 Post 的關聯
}

@Entity
public class Comment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String content;
    
    // TODO: 添加與 User 和 Post 的關聯
}
```

**答案:**
```java
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    
    @OneToMany(mappedBy = "author", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Post> posts = new ArrayList<>();
    
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Comment> comments = new ArrayList<>();
}

@Entity
public class Post {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String content;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "author_id", nullable = false)
    private User author;
    
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(
        name = "post_tags",
        joinColumns = @JoinColumn(name = "post_id"),
        inverseJoinColumns = @JoinColumn(name = "tag_id")
    )
    private Set<Tag> tags = new HashSet<>();
    
    @OneToMany(mappedBy = "post", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Comment> comments = new ArrayList<>();
}

@Entity
public class Tag {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    
    @ManyToMany(mappedBy = "tags", fetch = FetchType.LAZY)
    private Set<Post> posts = new HashSet<>();
}

@Entity
public class Comment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String content;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;
}
```

#### 10.1.4 查詢語言 (15%)

**重點知識:**
- JPQL 語法和關鍵字
- 命名查詢：@NamedQuery
- 原生 SQL：@Query(nativeQuery = true)
- 參數綁定：位置參數和命名參數
- 聚合函數和 GROUP BY

**練習題:**

```java
// 題目 4: 寫出 JPQL 查詢來滿足以下需求

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    // 1. 查找用戶名包含特定字串的用戶
    @Query("SELECT u FROM User u WHERE ?")
    List<User> findByUsernameContaining(String keyword);
    
    // 2. 查找發佈文章數量超過指定數量的用戶
    @Query("SELECT u FROM User u WHERE ?")
    List<User> findUsersWithPostCountGreaterThan(int count);
    
    // 3. 查找最近 30 天內活躍的用戶（有發佈文章或評論）
    @Query("SELECT DISTINCT u FROM User u WHERE ?")
    List<User> findActiveUsersInLast30Days();
    
    // 4. 統計每個用戶的文章和評論總數
    @Query("SELECT u.username, COUNT(p), COUNT(c) FROM User u " +
           "LEFT JOIN u.posts p LEFT JOIN u.comments c " +
           "GROUP BY u.id, u.username")
    List<Object[]> getUserActivityStats();
}
```

**答案:**
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    // 1. 查找用戶名包含特定字串的用戶
    @Query("SELECT u FROM User u WHERE u.username LIKE %:keyword%")
    List<User> findByUsernameContaining(@Param("keyword") String keyword);
    
    // 2. 查找發佈文章數量超過指定數量的用戶
    @Query("SELECT u FROM User u WHERE SIZE(u.posts) > :count")
    List<User> findUsersWithPostCountGreaterThan(@Param("count") int count);
    
    // 3. 查找最近 30 天內活躍的用戶
    @Query("SELECT DISTINCT u FROM User u WHERE " +
           "EXISTS (SELECT p FROM Post p WHERE p.author = u AND p.createdAt >= :date) OR " +
           "EXISTS (SELECT c FROM Comment c WHERE c.user = u AND c.createdAt >= :date)")
    List<User> findActiveUsersInLast30Days(@Param("date") LocalDateTime date);
    
    // 4. 統計每個用戶的文章和評論總數
    @Query("SELECT new com.example.UserActivityDto(u.username, COUNT(DISTINCT p), COUNT(DISTINCT c)) " +
           "FROM User u LEFT JOIN u.posts p LEFT JOIN u.comments c " +
           "GROUP BY u.id, u.username")
    List<UserActivityDto> getUserActivityStats();
}
```

### 10.2 Python SQLAlchemy 認證重點

#### 10.2.1 核心概念測驗

```python
# 題目 5: 以下程式碼的輸出是什麼？

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# 創建新用戶
user = User(username='test_user', email='test@example.com')
print(f"1. user in session: {user in session}")

session.add(user)
print(f"2. user in session: {user in session}")
print(f"3. user.id: {user.id}")

session.flush()
print(f"4. user.id: {user.id}")

session.commit()
print(f"5. user.id: {user.id}")

session.expunge(user)
print(f"6. user in session: {user in session}")
```

**答案:**
1. False (對象尚未添加到 session)
2. True (對象已添加但未提交)
3. None (ID 尚未生成)
4. [生成的ID] (flush 後 ID 已生成)
5. [相同的ID] (提交後 ID 保持不變)
6. False (對象已從 session 中移除)

#### 10.2.2 關聯對映測驗

```python
# 題目 6: 修正以下 SQLAlchemy 模型的錯誤

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    # 錯誤：缺少正確的關聯設定
    books = relationship("Book")

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    
    # 錯誤：缺少外鍵
    author = relationship("Author")

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    
    # 錯誤：多對多關聯缺少聯結表
    books = relationship("Book")
```

**答案:**
```python
# 聯結表定義
book_categories = Table(
    'book_categories', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    # 修正：添加 back_populates
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    
    # 修正：添加外鍵和 back_populates
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    
    # 修正：多對多關聯
    categories = relationship("Category", secondary=book_categories, back_populates="books")

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    
    # 修正：多對多關聯
    books = relationship("Book", secondary=book_categories, back_populates="categories")
```

### 10.3 認證考試準備策略

#### 10.3.1 學習計劃 (8週)

```mermaid
gantt
    title ORM 認證考試準備計劃
    dateFormat  YYYY-MM-DD
    section 基礎知識 (週1-2)
    ORM 概念與原理     :done, week1, 2024-01-01, 1w
    實體對映基礎       :done, week2, 2024-01-08, 1w
    
    section 進階功能 (週3-4)
    關聯對映深入       :active, week3, 2024-01-15, 1w
    查詢語言與 API     :week4, 2024-01-22, 1w
    
    section 效能優化 (週5-6)
    快取與載入策略     :week5, 2024-01-29, 1w
    查詢優化技巧       :week6, 2024-02-05, 1w
    
    section 實戰練習 (週7-8)
    綜合專案練習       :week7, 2024-02-12, 1w
    模擬考試與複習     :week8, 2024-02-19, 1w
```

#### 10.3.2 重點複習檢查表

**Java JPA/Hibernate 檢查表:**

- [ ] 理解 JPA 規範與 Hibernate 實作的差異
- [ ] 熟練掌握實體生命週期和狀態轉換
- [ ] 掌握所有對映註解的使用方法
- [ ] 理解不同關聯類型的配置和最佳實務
- [ ] 熟練編寫 JPQL 查詢
- [ ] 理解 Criteria API 的使用
- [ ] 掌握快取機制的配置和使用
- [ ] 理解交易管理和隔離等級
- [ ] 能夠識別和解決常見的效能問題

**Python SQLAlchemy 檢查表:**

- [ ] 理解 SQLAlchemy Core 和 ORM 的關係
- [ ] 熟練使用 declarative_base 定義模型
- [ ] 掌握不同類型的關聯定義方法
- [ ] 熟練使用 Session 進行資料操作
- [ ] 理解不同的載入策略及其適用場景
- [ ] 熟練編寫複雜的查詢表達式
- [ ] 掌握 Alembic 進行資料庫遷移
- [ ] 理解 SQLAlchemy 的快取機制
- [ ] 能夠進行查詢效能分析和優化

### 10.4 模擬考試題目

#### 10.4.1 綜合應用題 (Java)

```java
/**
 * 綜合題：設計一個線上學習平台的資料模型
 * 
 * 需求：
 * 1. 用戶可以註冊多個課程
 * 2. 課程包含多個章節
 * 3. 用戶可以完成章節並記錄進度
 * 4. 課程有分類
 * 5. 用戶可以對課程評分和評論
 * 
 * 請設計完整的實體模型，並回答以下問題：
 * a) 如何避免 N+1 查詢問題？
 * b) 如何實作軟刪除？
 * c) 如何確保資料一致性？
 */

// 請完成實體設計...
```

#### 10.4.2 綜合應用題 (Python)

```python
"""
綜合題：實作一個電商系統的訂單管理

需求：
1. 設計 User、Product、Order、OrderItem 實體
2. 實作購物車功能
3. 實作庫存管理
4. 確保訂單建立的原子性
5. 實作查詢最佳化

請實作以下功能：
a) 添加商品到購物車
b) 建立訂單（扣除庫存）
c) 查詢用戶訂單歷史
d) 統計商品銷售數據
"""

# 請完成實作...
```

### 10.5 小結

- **認證重點**：覆蓋核心概念、實體對映、關聯管理和查詢最佳化
- **學習策略**：循序漸進，理論結合實作
- **考試技巧**：熟練掌握常用 API，理解底層原理

**準備建議：**

- 多做實際專案練習，加深理解
- 閱讀官方文件，掌握最新特性
- 參與社群討論，學習最佳實務
- 定期複習，鞏固重點知識

---

## 11. 結論與學習資源

### 11.1 學習總結

通過本教學手冊的學習，您應該已經掌握了 ORM 的核心概念和實務應用。讓我們回顧一下學習的重點：

```mermaid
mindmap
  root((ORM 技能樹))
    基礎概念
      ORM 原理
      實體對映
      基本 CRUD
    進階技能
      關聯對映
      查詢最佳化
      效能調校
    實務應用
      專案架構
      錯誤處理
      測試策略
    專業發展
      認證準備
      持續學習
      技術分享
```

### 11.2 推薦學習資源

#### 11.2.1 官方文件

**Java 生態系統:**
- [JPA 2.2 規範](https://jcp.org/en/jsr/detail?id=338)
- [Hibernate 官方文件](https://hibernate.org/orm/documentation/)
- [Spring Data JPA 參考指南](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/)
- [Spring Boot 官方指南](https://spring.io/guides)

**Python 生態系統:**
- [SQLAlchemy 官方文件](https://docs.sqlalchemy.org/)
- [SQLAlchemy 教學](https://docs.sqlalchemy.org/en/14/tutorial/)
- [Alembic 文件](https://alembic.sqlalchemy.org/)
- [Django ORM 文件](https://docs.djangoproject.com/en/stable/topics/db/)

#### 11.2.2 推薦書籍

**Java 相關:**
1. **"Java Persistence with Hibernate"** - Christian Bauer, Gavin King
   - 深入的 Hibernate 實作指南
   - 涵蓋高級主題和最佳實務

2. **"Pro JPA 2"** - Mike Keith, Merrick Schincariol
   - JPA 規範的全面解析
   - 豐富的實例和案例研究

3. **"Spring Data"** - Mark Pollack, Oliver Gierke
   - Spring Data 生態系統完整介紹
   - 包含 JPA、MongoDB、Redis 等

**Python 相關:**
1. **"Essential SQLAlchemy"** - Jason Myers, Rick Copeland
   - SQLAlchemy 基礎到進階的完整指南
   - 實用的設計模式和最佳實務

2. **"Architecture Patterns with Python"** - Harry Percival, Bob Gregory
   - 包含 SQLAlchemy 在大型專案中的應用
   - 領域驅動設計和測試策略

#### 11.2.3 線上課程

**免費資源:**
- [Oracle JPA 教學](https://docs.oracle.com/javaee/6/tutorial/doc/bnbpz.html)
- [SQLAlchemy 官方教學](https://docs.sqlalchemy.org/en/14/tutorial/)
- [YouTube: ORM 概念解析](https://www.youtube.com/results?search_query=ORM+tutorial)

**付費平台:**
- Udemy: "Master Hibernate and JPA"
- Pluralsight: "SQLAlchemy Fundamentals"
- Coursera: "Database Systems" 課程

#### 11.2.4 實務工具

**開發工具:**
- IntelliJ IDEA (Java 開發)
- PyCharm (Python 開發)
- VS Code (通用編輯器)
- DBeaver (資料庫管理)

**效能監控:**
- JProfiler (Java 效能分析)
- Spring Boot Actuator (應用監控)
- SQLAlchemy-Utils (Python 工具集)
- pgAdmin/MySQL Workbench (資料庫監控)

**測試工具:**
- JUnit 5 + Testcontainers (Java 測試)
- pytest + factory_boy (Python 測試)
- H2 Database (記憶體資料庫測試)

### 11.3 持續學習建議

#### 11.3.1 技術發展趨勢

```mermaid
timeline
    title ORM 技術發展趨勢
    
    2020 : Reactive Programming
         : R2DBC (Reactive Relational Database Connectivity)
         : Spring WebFlux + R2DBC
    
    2021 : Cloud Native
         : Kubernetes 原生資料庫
         : 微服務資料存取模式
    
    2022 : AI/ML Integration
         : 智慧查詢最佳化
         : 自動索引建議
    
    2023 : Performance Focus
         : GraalVM 原生映像
         : 更快的啟動時間
    
    2024 : Modern Standards
         : JPA 3.1+ 新特性
         : SQLAlchemy 2.0+ 穩定版
```

#### 11.3.2 進階學習路徑

**專業深化方向:**

1. **效能專家路線**
   - 深入資料庫內核原理
   - 查詢計劃分析
   - 分散式資料庫設計

2. **架構師路線**
   - 微服務資料架構
   - CQRS 和 Event Sourcing
   - 資料治理和合規

3. **DevOps 整合**
   - 資料庫 CI/CD 流程
   - 監控和告警系統
   - 災難恢復策略

#### 11.3.3 社群參與

**推薦社群:**
- Stack Overflow ORM 標籤
- Reddit r/programming
- Hibernate 社群論壇
- SQLAlchemy Google 群組

**技術會議:**
- JavaOne (Oracle)
- PyCon (Python Conference)
- QCon (軟體架構會議)
- 本地 JUG (Java User Group)

### 11.4 實務專案建議

#### 11.4.1 入門專案

1. **個人部落格系統**
   - 用戶管理、文章發佈
   - 分類標籤、評論系統
   - 練習基本 CRUD 和關聯對映

2. **圖書管理系統**
   - 圖書借閱、用戶管理
   - 庫存追蹤、借閱歷史
   - 練習複雜查詢和報表

#### 11.4.2 進階專案

1. **電商平台**
   - 商品管理、訂單處理
   - 庫存管理、支付整合
   - 練習交易管理和效能最佳化

2. **學習管理系統**
   - 課程管理、學員進度
   - 考試評分、證書頒發
   - 練習複雜業務邏輯和資料分析

### 11.5 職涯發展建議

#### 11.5.1 技能認證

**Java 認證:**
- Oracle Certified Professional (OCP)
- Spring Professional Certification
- Hibernate 相關認證

**Python 認證:**
- Python Institute Certifications
- Django/Flask 框架認證

#### 11.5.2 作品集建構

**開源貢獻:**
- 參與 ORM 框架開發
- 撰寫技術部落格
- 創建教學資源

**商業專案:**
- 展示最佳實務應用
- 記錄效能最佳化成果
- 分享架構設計決策

### 11.6 最終建議

ORM 技術的學習是一個持續的過程，隨著業務需求的變化和技術的發展，需要不斷更新知識和技能。記住以下幾點：

1. **理論與實務並重** - 不僅要了解 ORM 的工作原理，更要在實際專案中應用
2. **效能意識** - 始終關注查詢效能和資源使用，養成良好的最佳化習慣
3. **安全第一** - 重視資料安全和隱私保護，遵循相關法規要求
4. **團隊協作** - 建立團隊程式碼規範，促進知識分享和技術傳承

希望本教學手冊能夠幫助您在 ORM 的學習道路上取得成功！

---

## 12. 檢查清單

### 12.1 新專案啟動檢查清單

#### 12.1.1 環境設定 ✓

**Java 專案:**
- [ ] JDK 版本確認 (建議 17+)
- [ ] Maven/Gradle 依賴設定
- [ ] Spring Boot 版本選擇
- [ ] 資料庫驅動添加
- [ ] 連線參數配置
- [ ] Hibernate 屬性設定
- [ ] 日誌級別配置

**Python 專案:**
- [ ] Python 版本確認 (建議 3.8+)
- [ ] 虛擬環境建立
- [ ] SQLAlchemy 版本選擇
- [ ] 資料庫驅動安裝
- [ ] 連線字串配置
- [ ] Alembic 初始化
- [ ] 日誌設定

#### 12.1.2 實體設計 ✓

- [ ] 實體命名規則統一
- [ ] 主鍵策略選擇
- [ ] 外鍵約束設定
- [ ] 索引策略規劃
- [ ] 資料類型對映確認
- [ ] 預設值設定
- [ ] 非空約束檢查
- [ ] 唯一約束驗證

#### 12.1.3 關聯設計 ✓

- [ ] 關聯類型選擇正確
- [ ] Fetch 策略合理
- [ ] Cascade 操作設定
- [ ] OrphanRemoval 考慮
- [ ] 雙向關聯一致性
- [ ] 聯結表設計
- [ ] 中間實體考慮
- [ ] 循環引用避免

### 12.2 開發階段檢查清單

#### 12.2.1 程式碼品質 ✓

- [ ] 命名規則一致性
- [ ] 方法職責單一
- [ ] 異常處理完整
- [ ] 日誌記錄適當
- [ ] 註釋文件充分
- [ ] 程式碼重複消除
- [ ] 設計模式應用
- [ ] SOLID 原則遵循

#### 12.2.2 效能考量 ✓

- [ ] N+1 問題檢查
- [ ] 查詢結果分頁
- [ ] 索引使用確認
- [ ] 快取策略實施
- [ ] 批次操作使用
- [ ] 連線池設定
- [ ] 交易邊界明確
- [ ] 資源釋放確保

#### 12.2.3 安全性檢查 ✓

- [ ] SQL 注入防護
- [ ] 參數化查詢使用
- [ ] 敏感資料加密
- [ ] 存取權限控制
- [ ] 資料驗證實施
- [ ] 錯誤訊息安全
- [ ] 日誌資料脫敏
- [ ] GDPR 合規考慮

### 12.3 測試階段檢查清單

#### 12.3.1 單元測試 ✓

- [ ] 實體類別測試
- [ ] Repository 測試
- [ ] Service 層測試
- [ ] 異常情況測試
- [ ] 邊界條件測試
- [ ] Mock 物件使用
- [ ] 測試資料隔離
- [ ] 測試覆蓋率檢查

#### 12.3.2 整合測試 ✓

- [ ] 資料庫整合測試
- [ ] 交易行為驗證
- [ ] 關聯載入測試
- [ ] 快取行為驗證
- [ ] 併發處理測試
- [ ] 效能基準測試
- [ ] 記憶體洩漏檢查
- [ ] 長時間運行測試

#### 12.3.3 資料測試 ✓

- [ ] 資料完整性驗證
- [ ] 約束條件測試
- [ ] 遷移腳本驗證
- [ ] 備份恢復測試
- [ ] 資料一致性檢查
- [ ] 參照完整性確認
- [ ] 資料清理驗證
- [ ] 存檔策略測試

### 12.4 部署前檢查清單

#### 12.4.1 生產環境準備 ✓

- [ ] 環境變數設定
- [ ] 連線參數確認
- [ ] SSL/TLS 配置
- [ ] 防火牆規則設定
- [ ] 監控系統部署
- [ ] 日誌收集配置
- [ ] 告警機制設定
- [ ] 備份策略確認

#### 12.4.2 效能最佳化 ✓

- [ ] 連線池調校
- [ ] 快取配置最佳化
- [ ] JVM 參數調整 (Java)
- [ ] 資料庫索引建立
- [ ] 查詢計劃檢查
- [ ] 慢查詢監控
- [ ] 資源使用監控
- [ ] 負載測試執行

#### 12.4.3 安全加固 ✓

- [ ] 資料庫用戶權限最小化
- [ ] 網路存取限制
- [ ] 敏感資料加密
- [ ] 審計日誌啟用
- [ ] 安全掃描執行
- [ ] 弱點評估完成
- [ ] 滲透測試驗證
- [ ] 合規檢查通過

### 12.5 維運階段檢查清單

#### 12.5.1 日常監控 ✓

- [ ] 應用效能監控
- [ ] 資料庫效能監控
- [ ] 錯誤率追蹤
- [ ] 資源使用監控
- [ ] 使用者行為分析
- [ ] 安全事件監控
- [ ] 備份狀態檢查
- [ ] 容量規劃更新

#### 12.5.2 定期維護 ✓

- [ ] 資料庫統計更新
- [ ] 索引重建評估
- [ ] 資料清理執行
- [ ] 日誌輪替管理
- [ ] 安全補丁更新
- [ ] 相依套件更新
- [ ] 配置檢查更新
- [ ] 災難恢復演練

#### 12.5.3 持續改進 ✓

- [ ] 效能趨勢分析
- [ ] 用戶回饋收集
- [ ] 技術債務評估
- [ ] 架構演進規劃
- [ ] 新技術評估
- [ ] 團隊技能提升
- [ ] 最佳實務更新
- [ ] 知識分享促進

### 12.6 故障排除檢查清單

#### 12.6.1 常見問題診斷 ✓

- [ ] 應用日誌檢查
- [ ] 資料庫日誌檢查
- [ ] 系統資源使用
- [ ] 網路連線狀態
- [ ] 設定檔案驗證
- [ ] 版本相容性確認
- [ ] 權限設定檢查
- [ ] 環境變數確認

#### 12.6.2 效能問題排查 ✓

- [ ] 慢查詢識別
- [ ] 索引使用分析
- [ ] 執行計劃檢查
- [ ] 快取命中率分析
- [ ] 記憶體使用分析
- [ ] CPU 使用模式
- [ ] IO 瓶頸識別
- [ ] 網路延遲測量

#### 12.6.3 資料問題處理 ✓

- [ ] 資料完整性檢查
- [ ] 參照完整性驗證
- [ ] 重複資料識別
- [ ] 資料類型錯誤
- [ ] 編碼問題檢查
- [ ] 時區處理確認
- [ ] 資料遷移驗證
- [ ] 備份可用性確認

---

**恭喜！您已完成 ORM 物件關聯對映的完整學習。**

這份檢查清單將幫助您在實際專案中應用所學知識，確保 ORM 應用的品質和可靠性。建議將此檢查清單保存並在每個專案階段使用，持續改進您的 ORM 開發技能。

記住：優秀的 ORM 應用不僅需要正確的實作，更需要持續的監控、最佳化和維護。保持學習，與時俱進！

---

## 附錄：快速參考指南

### A.1 常用註解速查表

#### Java JPA 註解

| 註解 | 用途 | 範例 |
|------|------|------|
| `@Entity` | 標記實體類別 | `@Entity public class User {}` |
| `@Table` | 指定表格名稱 | `@Table(name = "users")` |
| `@Id` | 標記主鍵 | `@Id private Long id;` |
| `@GeneratedValue` | 主鍵生成策略 | `@GeneratedValue(strategy = GenerationType.IDENTITY)` |
| `@Column` | 欄位對映 | `@Column(name = "user_name", length = 50)` |
| `@OneToMany` | 一對多關聯 | `@OneToMany(mappedBy = "user")` |
| `@ManyToOne` | 多對一關聯 | `@ManyToOne @JoinColumn(name = "user_id")` |
| `@ManyToMany` | 多對多關聯 | `@ManyToMany @JoinTable(...)` |
| `@Transactional` | 交易邊界 | `@Transactional(readOnly = true)` |

#### Python SQLAlchemy 基礎

| 元素 | 用途 | 範例 |
|------|------|------|
| `Column` | 定義欄位 | `Column(Integer, primary_key=True)` |
| `String` | 字串類型 | `Column(String(50))` |
| `ForeignKey` | 外鍵 | `Column(Integer, ForeignKey('users.id'))` |
| `relationship` | 關聯定義 | `relationship("Order", back_populates="user")` |
| `backref` | 反向引用 | `relationship("User", backref="orders")` |

### A.2 效能最佳化檢查清單

#### 查詢最佳化 ✓

- [ ] 使用索引覆蓋常用查詢
- [ ] 避免 SELECT * 查詢
- [ ] 使用分頁限制結果集大小
- [ ] 合理使用 JOIN 和子查詢
- [ ] 避免 N+1 查詢問題

#### 關聯載入策略 ✓

- [ ] 預設使用 LAZY 載入
- [ ] 必要時使用 EAGER 載入
- [ ] 使用 JOIN FETCH 避免 N+1
- [ ] 考慮使用 DTO 投影查詢

#### 快取策略 ✓

- [ ] 一級快取 (Session Cache) 管理
- [ ] 二級快取 (Entity Cache) 配置
- [ ] 查詢快取使用
- [ ] 分散式快取考慮

### A.3 常見錯誤解決方案

#### LazyInitializationException

```java
// 問題：Session 已關閉後存取延遲載入屬性
// 解決方案1：在 @Transactional 方法內完成所有操作
@Transactional
public void processUser(Long userId) {
    User user = userRepository.findById(userId);
    user.getOrders().size(); // 在交易內觸發載入
}

// 解決方案2：使用 EntityGraph
@EntityGraph(attributePaths = {"orders"})
Optional<User> findByIdWithOrders(Long id);
```

#### N+1 查詢問題

```python
# 問題：迴圈中執行查詢
users = session.query(User).all()  # 1 query
for user in users:
    print(len(user.orders))  # N queries

# 解決方案：使用 selectinload
users = session.query(User).options(selectinload(User.orders)).all()
```

### A.4 配置範本

#### application.yml (Spring Boot)

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
    username: ${DB_USER:user}
    password: ${DB_PASSWORD:password}
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
    properties:
      hibernate:
        format_sql: true
        dialect: org.hibernate.dialect.MySQL8Dialect
```

#### SQLAlchemy 配置 (Python)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/mydb"

engine = create_engine(
    DATABASE_URL,
    echo=False,  # 生產環境設為 False
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600
)

SessionLocal = sessionmaker(bind=engine)
```

---

**感謝您完成 ORM 教學手冊的學習！**

這份文件將持續更新以反映最新的技術發展和最佳實務。如有任何問題或建議，歡迎回饋。

**版本資訊**：
- 文件版本：v1.0
- 最後更新：2025年9月1日
- 作者：資深軟體架構師團隊
- 適用對象：Java 開發人員、系統架構師