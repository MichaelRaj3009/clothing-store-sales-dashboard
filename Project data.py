import pandas as pd
import matplotlib.pyplot as plt

# ---- DATA ----
data = {
    "Product":  ["T-Shirt", "Jeans", "Kurta", "Saree", "Jacket",
                 "Leggings", "Churidar", "Shorts", "Frock", "Blazer"],
    "Category": ["Men", "Men", "Women", "Women", "Men",
                 "Women", "Women", "Men", "Kids", "Men"],
    "Price":    [299, 899, 599, 1299, 1499,
                 349, 499, 249, 399, 2199],
    "Units_Sold": [45, 30, 50, 20, 15,
                   40, 35, 25, 30, 10]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Units_Sold"]

# ---- ANALYSIS ----
total_revenue     = df["Total_Sales"].sum()
best_product      = df.loc[df["Total_Sales"].idxmax(), "Product"]
most_sold         = df.loc[df["Units_Sold"].idxmax(), "Product"]
avg_price         = df["Price"].mean()
category_sales    = df.groupby("Category")["Total_Sales"].sum()

print("=" * 40)
print("   CLOTHING STORE — SALES SUMMARY")
print("=" * 40)
print(f"  Total Revenue    : ₹{total_revenue:,}")
print(f"  Best Seller      : {best_product}")
print(f"  Most Units Sold  : {most_sold}")
print(f"  Average Price    : ₹{avg_price:.0f}")
print("=" * 40)

# ---- DASHBOARD ----
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Clothing Store Sales Dashboard",
             fontsize=20, fontweight="bold", color="#2d3436", y=1.01)
fig.patch.set_facecolor("#f8f9fa")

colors_bar  = ["#6c5ce7","#a29bfe","#fd79a8","#e17055",
               "#00b894","#0984e3","#fdcb6e","#d63031","#00cec9","#2d3436"]

# Chart 1 — Total Sales by Product
axes[0,0].bar(df["Product"], df["Total_Sales"], color=colors_bar, edgecolor="white")
axes[0,0].set_title("Total Sales by Product (₹)", fontweight="bold")
axes[0,0].set_xlabel("Product")
axes[0,0].set_ylabel("Total Sales (₹)")
axes[0,0].tick_params(axis="x", rotation=45)
axes[0,0].set_facecolor("#f8f9fa")
for i, v in enumerate(df["Total_Sales"]):
    axes[0,0].text(i, v + 200, f"₹{v:,}", ha="center", fontsize=8)

# Chart 2 — Pie Chart by Category
pie_colors = ["#6c5ce7", "#fd79a8", "#00b894"]
axes[0,1].pie(category_sales, labels=category_sales.index,
              autopct="%1.1f%%", colors=pie_colors,
              startangle=140, wedgeprops={"edgecolor":"white","linewidth":2})
axes[0,1].set_title("Revenue Share by Category", fontweight="bold")

# Chart 3 — Units Sold
axes[1,0].barh(df["Product"], df["Units_Sold"], color=colors_bar, edgecolor="white")
axes[1,0].set_title("Units Sold per Product", fontweight="bold")
axes[1,0].set_xlabel("Units Sold")
axes[1,0].set_facecolor("#f8f9fa")
for i, v in enumerate(df["Units_Sold"]):
    axes[1,0].text(v + 0.3, i, str(v), va="center", fontsize=9)

# Chart 4 — Summary Stats Card
axes[1,1].axis("off")
axes[1,1].set_facecolor("#f8f9fa")
summary = (
    f"SALES SUMMARY\n\n"
    f"Total Revenue\n₹{total_revenue:,}\n\n"
    f"Best Selling Product\n{best_product}\n\n"
    f"Most Units Sold\n{most_sold}\n\n"
    f"Average Product Price\n₹{avg_price:.0f}"
)
axes[1,1].text(0.5, 0.5, summary,
               transform=axes[1,1].transAxes,
               fontsize=13, verticalalignment="center",
               horizontalalignment="center",
               bbox=dict(boxstyle="round,pad=1", facecolor="#6c5ce7",
                         alpha=0.15, edgecolor="#6c5ce7", linewidth=2),
               linespacing=1.8)

plt.tight_layout()
plt.savefig("clothing_dashboard_v2.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nDashboard saved as clothing_dashboard_v2.png ✅")
