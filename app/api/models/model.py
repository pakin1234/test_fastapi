from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, Float

metadata = MetaData()

categories = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("price", Float),
    Column("description", String),
    Column("category_id", Integer, ForeignKey("categories.id")),
)