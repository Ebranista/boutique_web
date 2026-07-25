import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Canvas class to generate 'Page X of Y' page numbers dynamically"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#7F8C8D"))
        
        # Header (Only on page 2 and later)
        if self._pageNumber > 1:
            self.drawString(54, 750, "Boutique Shop Management System — Database Design & Schema Specifications")
            self.setStrokeColor(colors.HexColor("#BDC3C7"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
        # Footer
        self.setFont("Helvetica", 8)
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 40, page_text)
        self.drawString(54, 40, "Confidential — Internal Developer Documentation")
        self.setStrokeColor(colors.HexColor("#BDC3C7"))
        self.setLineWidth(0.5)
        self.line(54, 52, 558, 52)
        
        self.restoreState()

def create_schema_pdf(filename="database_design.pdf"):
    # Target printable area: Letter size is 612 x 792 pt. 
    # Left/Right margins: 54pt (0.75 in). Printable width: 504pt.
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#2C3E50"),
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#7F8C8D"),
        spaceAfter=25
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#2C3E50"),
        spaceBefore=22,
        spaceAfter=12,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#34495E"),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#34495E"),
        spaceAfter=10
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#34495E"),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )
    
    th_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.white
    )
    
    td_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#2C3E50")
    )
    
    td_bold_style = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#2C3E50")
    )

    story = []
    
    # ------------------- TITLE PAGE / HEADER -------------------
    story.append(Spacer(1, 20))
    story.append(Paragraph("Boutique Shop Management System", title_style))
    story.append(Paragraph("System Architecture, Entity Relationships & Database Design Document", subtitle_style))
    story.append(Spacer(1, 10))
    
    # Introduction
    intro_text = (
        "<b>Introduction:</b><br/>"
        "This document details the database architecture, design choices, business validation rules, "
        "and schemas for the Boutique Shop Management System backend. It is designed to act as a complete "
        "technical specification for database developers and system integrators. The database is built on "
        "a highly normalized schema with robust constraints to ensure absolute data consistency."
    )
    story.append(Paragraph(intro_text, body_style))
    
    # Conceptual Schema Areas Diagram
    story.append(Paragraph("<b>Conceptual Schema Areas Diagram:</b>", h2_style))
    
    # ReportLab Drawing
    d = Drawing(504, 210)
    # Background card
    d.add(Rect(0, 0, 504, 210, fillColor=colors.HexColor("#F8F9F9"), strokeColor=colors.HexColor("#BDC3C7"), strokeWidth=0.5, rx=5, ry=5))
    
    # Helper for box group
    def draw_box(x, y, w, h, title, subtitle, color_hex):
        g = Group()
        g.add(Rect(x, y, w, h, fillColor=colors.HexColor(color_hex), strokeColor=None, rx=3, ry=3))
        g.add(String(x + w/2, y + h - 22, title, textAnchor='middle', fontName='Helvetica-Bold', fontSize=10, fillColor=colors.white))
        g.add(String(x + w/2, y + 14, subtitle, textAnchor='middle', fontName='Helvetica', fontSize=7.5, fillColor=colors.HexColor("#ECF0F1")))
        return g
        
    # Boxes
    d.add(draw_box(15, 125, 140, 55, "Auth & RBAC", "Users, Roles, Perms, Logs", "#34495E"))
    d.add(draw_box(182, 125, 140, 55, "Catalog & Products", "Products, Brands, Cats", "#2980B9"))
    d.add(draw_box(349, 125, 140, 55, "Inventory & Stocks", "Inventory, Movements", "#27AE60"))
    
    d.add(draw_box(15, 25, 140, 55, "Finance & Ops", "Capital, Expenses, Settings", "#8E44AD"))
    d.add(draw_box(182, 25, 140, 55, "POS & Sales", "Sales, Items, Customers", "#D35400"))
    d.add(draw_box(349, 25, 140, 55, "Purchasing", "Purchases, Suppliers", "#16A085"))
    
    # Lines (Relations)
    # Catalog to Inventory
    d.add(Line(322, 152, 349, 152, strokeColor=colors.HexColor("#7F8C8D"), strokeWidth=1))
    # Catalog to POS
    d.add(Line(252, 125, 252, 80, strokeColor=colors.HexColor("#7F8C8D"), strokeWidth=1))
    # Inventory to Purchasing
    d.add(Line(419, 125, 419, 80, strokeColor=colors.HexColor("#7F8C8D"), strokeWidth=1))
    # POS to Finance
    d.add(Line(182, 52, 155, 52, strokeColor=colors.HexColor("#7F8C8D"), strokeWidth=1))
    # Auth to Finance
    d.add(Line(85, 125, 85, 80, strokeColor=colors.HexColor("#7F8C8D"), strokeWidth=1))
    
    story.append(d)
    story.append(Spacer(1, 10))
    
    # Core Architecture Choice
    arch_text = (
        "<b>Core Database Design Decisions:</b><br/>"
        "• <b>UUID Primary Keys</b>: All tables use universally unique identifiers (UUIDs) stored as 36-character "
        "strings (mapped to VARCHAR(36) in MySQL). This facilitates horizontal scalability, prevents ID guessing "
        "attacks, and allows offline clients (like mobile POS apps) to generate unique record keys without a database roundtrip.<br/>"
        "• <b>Soft-Deletion Policy</b>: Rather than hard deleting entries (which damages financial histories "
        "and audit trails), the system utilizes soft deletion. Deleting a record sets `is_deleted = True` and "
        "records the timestamp in `deleted_at`. SQLAlchemy queries automatically filter out soft-deleted records by default.<br/>"
        "• <b>State Delta Auditing</b>: Database mutations are logged to the `audit_logs` table. This stores a "
        "JSON-encoded snapshot of the row state before (`old_value`) and after (`new_value`) the update, "
        "along with the actor's ID, request route, IP address, and client details."
    )
    story.append(Paragraph(arch_text, body_style))
    
    # Business Logic Section
    biz_text = (
        "<b>Business Rules & Constraints Enforced:</b><br/>"
        "• <b>Non-Negative Stock</b>: Stock values are validated at both the API and database levels. Inventory levels "
        "cannot drop below zero. Stock additions and subtractions generate immutable history logs.<br/>"
        "• <b>Valuation Math</b>: Stock purchase costs adjust a weighted `average_cost` inside the `inventory` table, "
        "calculating total financial inventory valuation (`average_cost * quantity`).<br/>"
        "• <b>Sales-Profit Coupling</b>: Creating a sale automatically reduces inventory levels, "
        "copies the item's purchase unit cost into `sale_items.unit_cost` (fixing the cost snapshot in case prices change "
        "later), calculates the net profit margin, and registers the cash flow in the active `capital` ledger.<br/>"
        "• <b>Price Integrity</b>: Buying wholesale price cannot exceed POS selling price without explicitly overridden "
        "Administrator permissions."
    )
    story.append(Paragraph(biz_text, body_style))
    
    # Relationship Description
    rel_text = (
        "<b>Entity-Relationship Overview:</b><br/>"
        "• <b>One-to-Many Relationships</b>: Categories to Products, Brands to Products, Users to Products (created by), "
        "Users to Sales (cashier), Customers to Sales, Sales to SaleItems, Suppliers to Products/Purchases, Purchases to PurchaseItems, "
        "ExpenseCategories to Expenses, and Users to AuditLogs.<br/>"
        "• <b>Many-to-Many Relationships</b>: Users to Roles (via `user_roles`), and Roles to Permissions (via `role_permissions`).<br/>"
        "• <b>One-to-One Relationships</b>: Products to Inventory."
    )
    story.append(Paragraph(rel_text, body_style))
    
    story.append(PageBreak())

    # Helper to generate table flowable
    def make_schema_table(table_name, columns):
        # Printable width is 504pt.
        # Column sizing: Column (110pt), Type (100pt), Constraints (110pt), Description (184pt)
        col_widths = [110, 100, 110, 184]
        
        table_data = [[
            Paragraph("Column", th_style),
            Paragraph("Data Type", th_style),
            Paragraph("Constraints", th_style),
            Paragraph("Description", th_style)
        ]]
        
        for col in columns:
            name_p = Paragraph(f"<b>{col[0]}</b>" if col[2] and "PRIMARY KEY" in col[2] else col[0], td_bold_style if col[2] and "PRIMARY KEY" in col[2] else td_style)
            type_p = Paragraph(col[1], td_style)
            const_p = Paragraph(col[2] if col[2] else "-", td_style)
            desc_p = Paragraph(col[3] if col[3] else "-", td_style)
            table_data.append([name_p, type_p, const_p, desc_p])
            
        t = Table(table_data, colWidths=col_widths, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2C3E50")),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BOTTOMPADDING', (0,0), (-1,0), 6),
            ('TOPPADDING', (0,0), (-1,0), 6),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8F9F9")]),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#BDC3C7")),
            ('TOPPADDING', (0,1), (-1,-1), 4),
            ('BOTTOMPADDING', (0,1), (-1,-1), 4),
        ]))
        return t

    # ------------------- SECTION 1: AUTH & RBAC -------------------
    story.append(Paragraph("1. Authentication & RBAC Modules", h1_style))
    
    # Table: users
    users_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique User identifier (UUID)"),
        ("username", "VARCHAR(50)", "UNIQUE, INDEX, NOT NULL", "Unique username for system login"),
        ("email", "VARCHAR(100)", "UNIQUE, INDEX, NOT NULL", "User email address"),
        ("password_hash", "VARCHAR(255)", "NOT NULL", "Bcrypt hashed password"),
        ("first_name", "VARCHAR(50)", "NOT NULL", "First name"),
        ("last_name", "VARCHAR(50)", "NOT NULL", "Last name"),
        ("phone", "VARCHAR(20)", "Nullable", "Contact number"),
        ("address", "VARCHAR(255)", "Nullable", "Home/office address"),
        ("profile_image", "VARCHAR(255)", "Nullable", "Path to profile picture"),
        ("is_active", "BOOLEAN", "DEFAULT True, NOT NULL", "Indicates if user account is enabled"),
        ("last_login", "DATETIME", "Nullable", "Timestamp of last successful login")
    ]
    story.append(KeepTogether([
        Paragraph("users Table", h2_style),
        Paragraph("Holds credentials and profiles for cashiers, managers, and administrators.", body_style),
        make_schema_table("users", users_cols)
    ]))
    story.append(Spacer(1, 15))
    
    # Table: roles
    roles_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Role identifier (UUID)"),
        ("name", "VARCHAR(50)", "UNIQUE, NOT NULL", "Role name (Administrator, Manager, Cashier)"),
        ("description", "VARCHAR(255)", "Nullable", "Brief role capability description")
    ]
    story.append(KeepTogether([
        Paragraph("roles Table", h2_style),
        Paragraph("Predefined user authorization tiers.", body_style),
        make_schema_table("roles", roles_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: permissions
    perms_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Permission identifier (UUID)"),
        ("name", "VARCHAR(100)", "UNIQUE, NOT NULL", "Unique permission string (e.g. manage_sales)"),
        ("description", "VARCHAR(255)", "Nullable", "Description of what it permits"),
        ("module", "VARCHAR(50)", "NOT NULL", "Associated module (sales, products, etc.)")
    ]
    story.append(KeepTogether([
        Paragraph("permissions Table", h2_style),
        Paragraph("Granular application capabilities checking.", body_style),
        make_schema_table("permissions", perms_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: user_roles
    user_roles_cols = [
        ("user_id", "VARCHAR(36)", "FOREIGN KEY(users.id), NOT NULL", "Associated User UUID"),
        ("role_id", "VARCHAR(36)", "FOREIGN KEY(roles.id), NOT NULL", "Associated Role UUID")
    ]
    story.append(KeepTogether([
        Paragraph("user_roles Table (Association Table)", h2_style),
        Paragraph("Establishes many-to-many joins between users and roles.", body_style),
        make_schema_table("user_roles", user_roles_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: role_permissions
    role_perms_cols = [
        ("role_id", "VARCHAR(36)", "FOREIGN KEY(roles.id), NOT NULL", "Associated Role UUID"),
        ("permission_id", "VARCHAR(36)", "FOREIGN KEY(permissions.id), NOT NULL", "Associated Permission UUID")
    ]
    story.append(KeepTogether([
        Paragraph("role_permissions Table (Association Table)", h2_style),
        Paragraph("Establishes many-to-many joins between roles and permissions.", body_style),
        make_schema_table("role_permissions", role_perms_cols)
    ]))
    
    story.append(PageBreak())

    # ------------------- SECTION 2: CATALOG & INVENTORY -------------------
    story.append(Paragraph("2. Catalog & Inventory Modules", h1_style))

    # Table: categories
    cat_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Category identifier (UUID)"),
        ("name", "VARCHAR(50)", "UNIQUE, INDEX, NOT NULL", "Category name (e.g. Dresses, Accessories)"),
        ("description", "VARCHAR(255)", "Nullable", "Category description")
    ]
    story.append(KeepTogether([
        Paragraph("categories Table", h2_style),
        Paragraph("Product categorization hierarchy.", body_style),
        make_schema_table("categories", cat_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: brands
    brand_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Brand identifier (UUID)"),
        ("name", "VARCHAR(50)", "UNIQUE, INDEX, NOT NULL", "Brand label name (e.g. Nike, Zara)"),
        ("description", "VARCHAR(255)", "Nullable", "Brand description")
    ]
    story.append(KeepTogether([
        Paragraph("brands Table", h2_style),
        Paragraph("Product designer/label categorization.", body_style),
        make_schema_table("brands", brand_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: products
    prod_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Product identifier (UUID)"),
        ("product_code", "VARCHAR(20)", "UNIQUE, INDEX, NOT NULL", "Auto-generated PRD-XXXXXXXX code"),
        ("barcode", "VARCHAR(50)", "UNIQUE, INDEX, Nullable", "Literal barcode text scanned/stored"),
        ("qr_code", "VARCHAR(255)", "UNIQUE, Nullable", "Optional path/reference to QR code"),
        ("name", "VARCHAR(100)", "INDEX, NOT NULL", "Product name label"),
        ("description", "TEXT", "Nullable", "Long product description details"),
        ("category_id", "VARCHAR(36)", "FOREIGN KEY(categories.id), NOT NULL", "Classification category link"),
        ("brand_id", "VARCHAR(36)", "FOREIGN KEY(brands.id), NOT NULL", "Classification brand link"),
        ("gender", "VARCHAR(10)", "DEFAULT 'unisex', NOT NULL", "Target segment (men, women, kids, unisex)"),
        ("color", "VARCHAR(50)", "Nullable", "Product color attribute"),
        ("size", "VARCHAR(20)", "Nullable", "Product size attribute (S, M, L, XL, etc.)"),
        ("buying_price", "DECIMAL(10,2)", "NOT NULL", "Item wholesale buying cost"),
        ("selling_price", "DECIMAL(10,2)", "NOT NULL", "Item POS retail selling price"),
        ("quantity", "INTEGER", "DEFAULT 0, NOT NULL", "Current inventory level"),
        ("minimum_stock", "INTEGER", "DEFAULT 10, NOT NULL", "Low stock indicator threshold level"),
        ("supplier_id", "VARCHAR(36)", "FOREIGN KEY(suppliers.id), Nullable", "Associated default supplier ID"),
        ("image", "VARCHAR(255)", "Nullable", "Link/path to product image"),
        ("status", "VARCHAR(20)", "DEFAULT 'active', NOT NULL", "Product state (active, inactive, discontinued)"),
        ("created_by", "VARCHAR(36)", "FOREIGN KEY(users.id), NOT NULL", "Admin/Staff user UUID who added it")
    ]
    story.append(KeepTogether([
        Paragraph("products Table", h2_style),
        Paragraph("Primary inventory item registry storing core item details and pricing information.", body_style),
        make_schema_table("products", prod_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: inventory
    inv_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Inventory identifier (UUID)"),
        ("product_id", "VARCHAR(36)", "FOREIGN KEY(products.id), UNIQUE, NOT NULL", "Associated Product UUID"),
        ("quantity", "INTEGER", "DEFAULT 0, NOT NULL", "Gross stock level count"),
        ("reserved_quantity", "INTEGER", "DEFAULT 0, NOT NULL", "Reserved stock for pending checkouts"),
        ("available_quantity", "INTEGER", "DEFAULT 0, NOT NULL", "Net sellable count (quantity - reserved)"),
        ("average_cost", "DECIMAL(10,2)", "DEFAULT 0.00", "Weighted average price of purchased items"),
        ("total_value", "DECIMAL(10,2)", "DEFAULT 0.00", "Total inventory financial asset valuation")
    ]
    story.append(KeepTogether([
        Paragraph("inventory Table", h2_style),
        Paragraph("Monitors available, reserved, and average costing valuation for products.", body_style),
        make_schema_table("inventory", inv_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: stock_movements
    mov_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique StockMovement identifier (UUID)"),
        ("inventory_id", "VARCHAR(36)", "FOREIGN KEY(inventory.id), NOT NULL", "Associated Inventory UUID"),
        ("product_id", "VARCHAR(36)", "FOREIGN KEY(products.id), NOT NULL", "Associated Product UUID"),
        ("movement_type", "VARCHAR(20)", "NOT NULL", "Log classification (stock_in, stock_out, adjustment)"),
        ("quantity", "INTEGER", "NOT NULL", "Quantity size of stock shift"),
        ("previous_quantity", "INTEGER", "NOT NULL", "Stock level prior to transaction"),
        ("new_quantity", "INTEGER", "NOT NULL", "Updated stock level post transaction"),
        ("reference_type", "VARCHAR(50)", "Nullable", "Audit source module (sale, purchase, adjustment)"),
        ("reference_id", "VARCHAR(36)", "Nullable", "Audit source module identifier link"),
        ("reason", "VARCHAR(255)", "Nullable", "Short descriptive text of movement"),
        ("notes", "TEXT", "Nullable", "Extended notes"),
        ("performed_by", "VARCHAR(36)", "FOREIGN KEY(users.id), NOT NULL", "Staff user UUID who made adjustment")
    ]
    story.append(KeepTogether([
        Paragraph("stock_movements Table", h2_style),
        Paragraph("Comprehensive inventory transaction logging table.", body_style),
        make_schema_table("stock_movements", mov_cols)
    ]))
    
    story.append(PageBreak())

    # ------------------- SECTION 3: SALES & POS -------------------
    story.append(Paragraph("3. Sales & POS Modules", h1_style))

    # Table: customers
    cust_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Customer identifier (UUID)"),
        ("name", "VARCHAR(100)", "INDEX, NOT NULL", "Customer full name"),
        ("phone", "VARCHAR(20)", "NOT NULL", "Contact phone number"),
        ("email", "VARCHAR(100)", "Nullable", "Email address"),
        ("address", "VARCHAR(255)", "Nullable", "Delivery/home address"),
        ("gender", "VARCHAR(10)", "Nullable", "Gender options (male, female, other)"),
        ("birthday", "DATE", "Nullable", "Birthday for tracking age & birthday promotions"),
        ("image", "VARCHAR(255)", "Nullable", "Path to profile picture"),
        ("loyalty_points", "INTEGER", "DEFAULT 0, NOT NULL", "Loyalty system accumulated points"),
        ("is_active", "BOOLEAN", "DEFAULT True, NOT NULL", "Account status flag")
    ]
    story.append(KeepTogether([
        Paragraph("customers Table", h2_style),
        Paragraph("Customer database recording profiles and loyalty reward program balances.", body_style),
        make_schema_table("customers", cust_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: sales
    sales_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Sale identifier (UUID)"),
        ("invoice_number", "VARCHAR(20)", "UNIQUE, INDEX, NOT NULL", "Unique invoice reference number"),
        ("receipt_number", "VARCHAR(20)", "UNIQUE, NOT NULL", "Unique receipt voucher string"),
        ("customer_id", "VARCHAR(36)", "FOREIGN KEY(customers.id), Nullable", "Customer UUID associated with sale"),
        ("subtotal", "DECIMAL(10,2)", "DEFAULT 0.00", "Gross purchase amount sum"),
        ("discount", "DECIMAL(10,2)", "DEFAULT 0.00", "Invoice deduction discount amount"),
        ("tax", "DECIMAL(10,2)", "DEFAULT 0.00", "Calculated tax size (18% by default)"),
        ("total", "DECIMAL(10,2)", "DEFAULT 0.00", "Net payable invoice sum"),
        ("payment_method", "VARCHAR(50)", "NOT NULL", "Payment type (cash, card, mobile_money, bank_transfer)"),
        ("cash_received", "DECIMAL(10,2)", "DEFAULT 0.00", "Cash amount handed over by customer"),
        ("change", "DECIMAL(10,2)", "DEFAULT 0.00", "Calculated return change amount"),
        ("total_cost", "DECIMAL(10,2)", "DEFAULT 0.00", "Aggregate item buying cost total for reporting"),
        ("total_profit", "DECIMAL(10,2)", "DEFAULT 0.00", "Net profit margin total"),
        ("status", "VARCHAR(20)", "DEFAULT 'completed', NOT NULL", "Voucher state (pending, completed, cancelled, refunded)"),
        ("sale_date", "DATETIME", "DEFAULT utcnow, NOT NULL", "Timestamp of point of sale completion"),
        ("notes", "TEXT", "Nullable", "Sale checkout notes"),
        ("cashier_id", "VARCHAR(36)", "FOREIGN KEY(users.id), NOT NULL", "Cashier/Staff user UUID who made checkout")
    ]
    story.append(KeepTogether([
        Paragraph("sales Table", h2_style),
        Paragraph("Financial headers for POS retail transactions.", body_style),
        make_schema_table("sales", sales_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: sale_items
    sale_item_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique SaleItem identifier (UUID)"),
        ("sale_id", "VARCHAR(36)", "FOREIGN KEY(sales.id), NOT NULL", "Parent Sale UUID link"),
        ("product_id", "VARCHAR(36)", "FOREIGN KEY(products.id), NOT NULL", "Purchased Product UUID link"),
        ("quantity", "INTEGER", "NOT NULL", "Volume bought"),
        ("unit_price", "DECIMAL(10,2)", "NOT NULL", "Unit price at POS time"),
        ("discount", "DECIMAL(10,2)", "DEFAULT 0.00", "Unit discount deduction applied"),
        ("subtotal", "DECIMAL(10,2)", "DEFAULT 0.00", "Subtotal amount (price * qty - discount)"),
        ("unit_cost", "DECIMAL(10,2)", "NOT NULL", "Unit buying price at POS time (fixed for profit reports)")
    ]
    story.append(KeepTogether([
        Paragraph("sale_items Table", h2_style),
        Paragraph("Itemized product checkout lines linked to sales.", body_style),
        make_schema_table("sale_items", sale_item_cols)
    ]))
    
    story.append(PageBreak())

    # ------------------- SECTION 4: PURCHASES & EXPENSES -------------------
    story.append(Paragraph("4. Purchasing & Expense Modules", h1_style))

    # Table: suppliers
    sup_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Supplier identifier (UUID)"),
        ("name", "VARCHAR(100)", "INDEX, NOT NULL", "Supplier business name"),
        ("contact_person", "VARCHAR(100)", "Nullable", "Supplier contact person"),
        ("phone", "VARCHAR(20)", "NOT NULL", "Business contact phone number"),
        ("email", "VARCHAR(100)", "Nullable", "Business contact email"),
        ("address", "VARCHAR(255)", "Nullable", "Factory/head office physical address"),
        ("tin_number", "VARCHAR(50)", "Nullable", "Tax Identification Number"),
        ("outstanding_balance", "DECIMAL(10,2)", "DEFAULT 0.00", "Debt balance owed to the supplier"),
        ("is_active", "BOOLEAN", "DEFAULT True, NOT NULL", "Supplier active status flag")
    ]
    story.append(KeepTogether([
        Paragraph("suppliers Table", h2_style),
        Paragraph("Registry of wholesale manufacturers/suppliers.", body_style),
        make_schema_table("suppliers", sup_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: purchases
    pur_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Purchase identifier (UUID)"),
        ("purchase_number", "VARCHAR(20)", "UNIQUE, INDEX, NOT NULL", "Unique purchase order document identifier"),
        ("supplier_id", "VARCHAR(36)", "FOREIGN KEY(suppliers.id), NOT NULL", "Associated Supplier UUID"),
        ("subtotal", "DECIMAL(10,2)", "DEFAULT 0.00", "Total items net cost sum"),
        ("discount", "DECIMAL(10,2)", "DEFAULT 0.00", "Total purchase order discount applied"),
        ("tax", "DECIMAL(10,2)", "DEFAULT 0.00", "Tax size calculated (18% by default)"),
        ("total", "DECIMAL(10,2)", "DEFAULT 0.00", "Total net cost payable"),
        ("payment_method", "VARCHAR(50)", "NOT NULL", "Payment type (cash, bank_transfer, credit)"),
        ("paid_amount", "DECIMAL(10,2)", "DEFAULT 0.00", "Amount paid immediately on order placement"),
        ("balance", "DECIMAL(10,2)", "DEFAULT 0.00", "Remaining unpaid balance (total - paid_amount)"),
        ("purchase_date", "DATETIME", "DEFAULT utcnow, NOT NULL", "Purchase order timestamp"),
        ("status", "VARCHAR(20)", "DEFAULT 'pending', NOT NULL", "Purchase state (pending, completed, cancelled)"),
        ("notes", "TEXT", "Nullable", "PO checkout notes"),
        ("receipt_image", "VARCHAR(255)", "Nullable", "Link/path to invoice PDF or image scan"),
        ("created_by", "VARCHAR(36)", "FOREIGN KEY(users.id), NOT NULL", "Staff user UUID who placed the PO")
    ]
    story.append(KeepTogether([
        Paragraph("purchases Table", h2_style),
        Paragraph("Financial headers for wholesale purchase orders made to restock catalog items.", body_style),
        make_schema_table("purchases", pur_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: purchase_items
    pur_item_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique PurchaseItem identifier (UUID)"),
        ("purchase_id", "VARCHAR(36)", "FOREIGN KEY(purchases.id), NOT NULL", "Parent Purchase UUID link"),
        ("product_id", "VARCHAR(36)", "FOREIGN KEY(products.id), NOT NULL", "Purchased Product UUID link"),
        ("quantity", "INTEGER", "NOT NULL", "Volume bought"),
        ("buying_price", "DECIMAL(10,2)", "NOT NULL", "Agreed unit buying cost"),
        ("discount", "DECIMAL(10,2)", "DEFAULT 0.00", "Unit discount applied"),
        ("subtotal", "DECIMAL(10,2)", "DEFAULT 0.00", "Subtotal cost (price * qty - discount)")
    ]
    story.append(KeepTogether([
        Paragraph("purchase_items Table", h2_style),
        Paragraph("Itemized product checkout lines linked to purchases.", body_style),
        make_schema_table("purchase_items", pur_item_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: expense_categories
    exp_cat_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Category identifier (UUID)"),
        ("name", "VARCHAR(50)", "UNIQUE, INDEX, NOT NULL", "Expense category name (Rent, Salary, etc.)"),
        ("description", "VARCHAR(255)", "Nullable", "Brief category explanation"),
        ("is_recurring", "BOOLEAN", "DEFAULT False, NOT NULL", "Indicates if categories are recurring monthly")
    ]
    story.append(KeepTogether([
        Paragraph("expense_categories Table", h2_style),
        Paragraph("Predefined operational expense classifications.", body_style),
        make_schema_table("expense_categories", exp_cat_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: expenses
    exp_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Expense identifier (UUID)"),
        ("name", "VARCHAR(100)", "NOT NULL", "Short title description of the expense"),
        ("description", "TEXT", "Nullable", "Long text expense details"),
        ("category_id", "VARCHAR(36)", "FOREIGN KEY(expense_categories.id), NOT NULL", "Associated Category UUID link"),
        ("amount", "DECIMAL(10,2)", "NOT NULL", "Amount cost"),
        ("expense_date", "DATETIME", "DEFAULT utcnow, NOT NULL", "Transaction billing date"),
        ("is_recurring", "BOOLEAN", "DEFAULT False, NOT NULL", "Indicates if expense is recurring"),
        ("recurring_month", "INTEGER", "Nullable", "Target month value for recurring items (1-12)"),
        ("receipt_image", "VARCHAR(255)", "Nullable", "Link to image scan of payment receipt"),
        ("notes", "TEXT", "Nullable", "Expense notes"),
        ("created_by", "VARCHAR(36)", "FOREIGN KEY(users.id), NOT NULL", "Staff user UUID who created the expense entry")
    ]
    story.append(KeepTogether([
        Paragraph("expenses Table", h2_style),
        Paragraph("Individual business operational expenditure records.", body_style),
        make_schema_table("expenses", exp_cols)
    ]))
    
    story.append(PageBreak())

    # ------------------- SECTION 5: CAPITAL, SETTINGS, AUDIT & NOTIFICATIONS -------------------
    story.append(Paragraph("5. Capital, Settings, Auditing & Notifications", h1_style))

    # Table: capital
    cap_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Capital ledger ID (UUID)"),
        ("beginning_capital", "DECIMAL(12,2)", "DEFAULT 0.00", "Starting account balance at period start"),
        ("current_capital", "DECIMAL(12,2)", "DEFAULT 0.00", "Active liquidity balance"),
        ("total_invested", "DECIMAL(12,2)", "DEFAULT 0.00", "Aggregated capital investment injects"),
        ("total_withdrawn", "DECIMAL(12,2)", "DEFAULT 0.00", "Aggregated owner capital drawings"),
        ("period_start", "DATETIME", "DEFAULT utcnow, NOT NULL", "Financial calendar period start"),
        ("period_end", "DATETIME", "Nullable", "Financial calendar period end"),
        ("is_active", "BOOLEAN", "DEFAULT True, NOT NULL", "Indicates active financial period")
    ]
    story.append(KeepTogether([
        Paragraph("capital Table", h2_style),
        Paragraph("Monitors current and cumulative capital ledger positions for financial modeling.", body_style),
        make_schema_table("capital", cap_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: settings
    set_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Settings row ID (UUID)"),
        ("shop_name", "VARCHAR(100)", "NOT NULL", "Retail shop commercial name"),
        ("logo", "VARCHAR(255)", "Nullable", "File path or URL to shop logo"),
        ("address", "VARCHAR(255)", "Nullable", "Retail shop commercial physical address"),
        ("phone", "VARCHAR(20)", "Nullable", "Shop contact telephone number"),
        ("email", "VARCHAR(100)", "Nullable", "Shop support email address"),
        ("currency", "VARCHAR(3)", "DEFAULT 'USD', NOT NULL", "Global base currency choice (e.g. USD, EUR)"),
        ("currency_symbol", "VARCHAR(5)", "DEFAULT '$', NOT NULL", "Global base currency printable symbol"),
        ("tax_percentage", "INTEGER", "DEFAULT 18, NOT NULL", "Global default tax percentage rate (integer value)"),
        ("receipt_header", "TEXT", "Nullable", "Custom print header text on physical receipts"),
        ("receipt_footer", "TEXT", "Nullable", "Custom print footer text on physical receipts"),
        ("low_stock_limit", "INTEGER", "DEFAULT 10, NOT NULL", "Default global inventory low alert threshold"),
        ("dark_mode", "BOOLEAN", "DEFAULT False, NOT NULL", "Default interface display theme setting"),
        ("tin_number", "VARCHAR(50)", "Nullable", "Tax Identification Number for receipt billing")
    ]
    story.append(KeepTogether([
        Paragraph("settings Table", h2_style),
        Paragraph("System configuration metadata parameters (typically single-row tables).", body_style),
        make_schema_table("settings", set_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: notifications
    notif_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique Notification identifier (UUID)"),
        ("user_id", "VARCHAR(36)", "FOREIGN KEY(users.id), NOT NULL", "Recipient User UUID link"),
        ("title", "VARCHAR(100)", "NOT NULL", "Notification title header text"),
        ("message", "TEXT", "NOT NULL", "Long message details"),
        ("notification_type", "VARCHAR(50)", "NOT NULL", "Category (low_stock, out_of_stock, expense_reminder, etc.)"),
        ("reference_type", "VARCHAR(50)", "Nullable", "Optional linked system module category"),
        ("reference_id", "VARCHAR(36)", "Nullable", "Optional linked system record ID"),
        ("is_read", "BOOLEAN", "DEFAULT False, NOT NULL", "Boolean indicating read status"),
        ("read_at", "DATETIME", "Nullable", "Timestamp when recipient marked as read"),
        ("push_sent", "BOOLEAN", "DEFAULT False, NOT NULL", "Boolean indicating Firebase push execution"),
        ("push_sent_at", "DATETIME", "Nullable", "Timestamp when push notification was dispatched")
    ]
    story.append(KeepTogether([
        Paragraph("notifications Table", h2_style),
        Paragraph("Stores alerts, notices, and integration logs for FCM Push messaging.", body_style),
        make_schema_table("notifications", notif_cols)
    ]))
    story.append(Spacer(1, 15))

    # Table: audit_logs
    aud_cols = [
        ("id", "VARCHAR(36)", "PRIMARY KEY, NOT NULL", "Unique AuditLog identifier (UUID)"),
        ("user_id", "VARCHAR(36)", "FOREIGN KEY(users.id), NOT NULL", "UUID of acting User"),
        ("username", "VARCHAR(50)", "NOT NULL", "Snapshot username of actor"),
        ("action", "VARCHAR(50)", "NOT NULL", "Classification of action (create, update, delete, login)"),
        ("entity_type", "VARCHAR(50)", "NOT NULL", "Target resource name (product, sale, user, etc.)"),
        ("entity_id", "VARCHAR(36)", "Nullable", "Target resource primary key value"),
        ("old_value", "TEXT", "Nullable", "JSON text representation of prior record state"),
        ("new_value", "TEXT", "Nullable", "JSON text representation of updated record state"),
        ("ip_address", "VARCHAR(45)", "Nullable", "IP Address of request client"),
        ("user_agent", "VARCHAR(255)", "Nullable", "Browser user agent metadata header"),
        ("request_method", "VARCHAR(10)", "Nullable", "HTTP Verb of request (POST, PUT, DELETE)"),
        ("request_path", "VARCHAR(255)", "Nullable", "HTTP Request routing path"),
        ("status", "VARCHAR(20)", "DEFAULT 'success', NOT NULL", "Status of log operation (success, failure)"),
        ("error_message", "TEXT", "Nullable", "Standard stack trace or error response message if failed")
    ]
    story.append(KeepTogether([
        Paragraph("audit_logs Table", h2_style),
        Paragraph("System action trace logs capturing row-level mutation changes.", body_style),
        make_schema_table("audit_logs", aud_cols)
    ]))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Full Schema and Database Design documentation generated at: {filename}")

if __name__ == "__main__":
    create_schema_pdf()
