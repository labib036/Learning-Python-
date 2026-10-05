import flet as ft

class ShopManagerApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Premium Inventory Manager"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.window_width = 1000
        self.page.window_height = 700
        self.page.padding = 0
        self.page.theme = ft.Theme(color_scheme_seed=ft.Colors.TEAL)

        # State Management
        self.inventory = [
            {"name": "Apple", "price": 10.0, "stock": 5},
            {"name": "Banana", "price": 8.0, "stock": 6},
            {"name": "Carrot", "price": 5.0, "stock": 10}
        ]
        self.revenue = 0.0

        # UI Components
        self.build_ui()

    def show_snackbar(self, message, color=ft.Colors.GREEN):
        snack = ft.SnackBar(ft.Text(message, color=ft.Colors.WHITE), bgcolor=color)
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def build_ui(self):
        # 1. Navigation Rail
        self.nav_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(icon=ft.Icons.DASHBOARD_OUTLINED, selected_icon=ft.Icons.DASHBOARD, label="Dashboard"),
                ft.NavigationRailDestination(icon=ft.Icons.INVENTORY_2_OUTLINED, selected_icon=ft.Icons.INVENTORY_2, label="Inventory"),
                ft.NavigationRailDestination(icon=ft.Icons.POINT_OF_SALE_OUTLINED, selected_icon=ft.Icons.POINT_OF_SALE, label="Sell (POS)"),
            ],
            on_change=self.nav_change,
        )

        # 2. Views Container
        self.view_container = ft.Container(
            expand=True,
            padding=30,
            content=self.get_dashboard_view()
        )

        # Main Layout
        main_layout = ft.Row(
            [
                self.nav_rail,
                ft.VerticalDivider(width=1),
                self.view_container
            ],
            expand=True,
        )
        self.page.add(main_layout)

    def nav_change(self, e):
        index = e.control.selected_index
        if index == 0:
            self.view_container.content = self.get_dashboard_view()
        elif index == 1:
            self.view_container.content = self.get_inventory_view()
        elif index == 2:
            self.view_container.content = self.get_pos_view()
        self.page.update()

    # ========================== VIEWS ==========================

    def get_dashboard_view(self):
        low_stock_items = [i for i in self.inventory if i["stock"] < 3]

        revenue_card = self.create_metric_card("Total Revenue", f"${self.revenue:.2f}", ft.Icons.ATTACH_MONEY, ft.Colors.TEAL)
        items_card = self.create_metric_card("Total Products", str(len(self.inventory)), ft.Icons.INVENTORY, ft.Colors.BLUE)
        alert_card = self.create_metric_card("Low Stock Alerts", str(len(low_stock_items)), ft.Icons.WARNING, ft.Colors.RED if low_stock_items else ft.Colors.GREEN)

        return ft.Column([
            ft.Text("Dashboard Overview", size=32, weight=ft.FontWeight.BOLD),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Row([revenue_card, items_card, alert_card], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
            ft.Text("Low Stock Items (Below 3)", size=20, weight=ft.FontWeight.W_600, color=ft.Colors.RED_300),
            ft.Column([ft.Text(f"• {item['name']} - Only {item['stock']} left!") for item in low_stock_items]) if low_stock_items else ft.Text("All stocks are healthy! 🎉", color=ft.Colors.GREEN)
        ], expand=True)

    def get_inventory_view(self):
        columns = [
            ft.DataColumn(ft.Text("Item Name")),
            ft.DataColumn(ft.Text("Price ($)"), numeric=True),
            ft.DataColumn(ft.Text("Stock"), numeric=True),
            ft.DataColumn(ft.Text("Actions")),
        ]

        rows = []
        for item in self.inventory:
            rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(item["name"])),
                    ft.DataCell(ft.Text(f"{item['price']:.2f}")),
                    ft.DataCell(ft.Text(str(item["stock"]))),
                    ft.DataCell(
                        ft.IconButton(icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE_200, tooltip="Edit Item", on_click=lambda e, i=item: self.open_edit_dialog(i))
                    ),
                ])
            )

        data_table = ft.DataTable(columns=columns, rows=rows, expand=True)

        return ft.Column([
            ft.Row([
                ft.Text("Inventory Management", size=32, weight=ft.FontWeight.BOLD),
                ft.FilledButton("Add New Item", icon=ft.Icons.ADD, on_click=self.open_add_dialog, style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL, color=ft.Colors.WHITE))
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(),
            ft.ListView([data_table], expand=True)
        ], expand=True)

    def get_pos_view(self):
        item_dropdown = ft.Dropdown(
            label="Select Product",
            options=[ft.dropdown.Option(item["name"]) for item in self.inventory],
            width=300
        )
        qty_input = ft.TextField(label="Quantity", width=150, keyboard_type=ft.KeyboardType.NUMBER)
        
        def process_sale(e):
            if not item_dropdown.value or not qty_input.value:
                self.show_snackbar("Please select an item and enter quantity.", ft.Colors.RED)
                return
            
            try:
                qty = int(qty_input.value)
                if qty <= 0: raise ValueError
            except:
                self.show_snackbar("Quantity must be a valid positive number.", ft.Colors.RED)
                return

            for item in self.inventory:
                if item["name"] == item_dropdown.value:
                    if qty > item["stock"]:
                        self.show_snackbar(f"Not enough stock! Only {item['stock']} available.", ft.Colors.RED)
                    else:
                        cost = item["price"] * qty
                        item["stock"] -= qty
                        self.revenue += cost
                        self.show_snackbar(f"Sold {qty}x {item['name']} for ${cost:.2f}", ft.Colors.GREEN)
                        qty_input.value = ""
                        self.page.update()
                    break

        return ft.Column([
            ft.Text("Point of Sale (Customer Buy)", size=32, weight=ft.FontWeight.BOLD),
            ft.Divider(height=30),
            ft.Row([item_dropdown, qty_input]),
            ft.FilledButton("Complete Sale", icon=ft.Icons.SHOPPING_CART_CHECKOUT, on_click=process_sale, height=50, style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL, color=ft.Colors.WHITE))
        ])

    def create_metric_card(self, title, value, icon, color):
        return ft.Card(
            elevation=4,
            content=ft.Container(
                padding=20,
                width=250,
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                border_radius=10,
                content=ft.Column([
                    ft.Icon(icon, size=40, color=color),
                    ft.Text(title, size=16, color=ft.Colors.ON_SURFACE_VARIANT),
                    ft.Text(value, size=28, weight=ft.FontWeight.BOLD)
                ])
            )
        )

    def open_add_dialog(self, e):
        name_in = ft.TextField(label="Item Name")
        price_in = ft.TextField(label="Price", keyboard_type=ft.KeyboardType.NUMBER)
        stock_in = ft.TextField(label="Stock", keyboard_type=ft.KeyboardType.NUMBER)

        def save_new_item(e):
            if not name_in.value or not price_in.value or not stock_in.value:
                self.show_snackbar("Please fill all fields.", ft.Colors.RED)
                return
            
            if any(i["name"].lower() == name_in.value.lower() for i in self.inventory):
                self.show_snackbar("Item already exists!", ft.Colors.RED)
                return

            try:
                price = float(price_in.value)
                stock = int(stock_in.value)
                self.inventory.append({"name": name_in.value.capitalize(), "price": price, "stock": stock})
                self.show_snackbar(f"Added {name_in.value} successfully!")
                dlg.open = False
                self.nav_change(type('Event', (object,), {'control': self.nav_rail}))
                self.page.update()
            except ValueError:
                self.show_snackbar("Price must be a number and Stock must be an integer.", ft.Colors.RED)

        dlg = ft.AlertDialog(
            title=ft.Text("Add New Item"),
            content=ft.Column([name_in, price_in, stock_in], tight=True),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: setattr(dlg, 'open', False) or self.page.update()),
                ft.FilledButton("Save", on_click=save_new_item, style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL, color=ft.Colors.WHITE)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.overlay.append(dlg)
        dlg.open = True
        self.page.update()

    def open_edit_dialog(self, item):
        price_in = ft.TextField(label="New Price", value=str(item["price"]), keyboard_type=ft.KeyboardType.NUMBER)
        stock_in = ft.TextField(label="New Stock", value=str(item["stock"]), keyboard_type=ft.KeyboardType.NUMBER)

        def save_edit(e):
            try:
                item["price"] = float(price_in.value)
                item["stock"] = int(stock_in.value)
                self.show_snackbar(f"Updated {item['name']} successfully!")
                dlg.open = False
                self.nav_change(type('Event', (object,), {'control': self.nav_rail}))
                self.page.update()
            except ValueError:
                self.show_snackbar("Invalid input. Try again.", ft.Colors.RED)

        dlg = ft.AlertDialog(
            title=ft.Text(f"Edit {item['name']}"),
            content=ft.Column([price_in, stock_in], tight=True),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: setattr(dlg, 'open', False) or self.page.update()),
                ft.FilledButton("Update", on_click=save_edit, style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)),
            ],
        )
        self.page.overlay.append(dlg)
        dlg.open = True
        self.page.update()

def main(page: ft.Page):
    ShopManagerApp(page)

ft.run(main)



def remove_students():
    print("--- Remove a Student ---")
    print("Enter The Name To Search:")
    search_name = input()
    
    count = 0
    for student_id, data in students.items():
        if search_name in data['name']:
            print("ID:", student_id, " | Name:", data['name'])
            count = count + 1
            
    if count == 0:
        print("Student not found!")
    else:
        print("Enter The Student ID You Want To Remove:")
        student_id_to_remove = input()
        
        if student_id_to_remove in students:
            print("Student found:", students[student_id_to_remove]['name'])
            print("Are You Sure? (y/n)")
            confirm = input()
            
            if confirm == "y":
                del students[student_id_to_remove]
                print("Student removed successfully!")
            else:
                print("Removal cancelled.")
        else:
            print("Invalid Student ID!")
        else:
            print("Removal cancelled.")
Do the remove Function as stated below
1.call and use the search by name function and allow it to show all the names and then allow the user to input the student id of the labib and then delte the whole student data            