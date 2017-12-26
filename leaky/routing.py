from channels import include


project_routing = [
    include("warehouses.routing.app_routing", path=r"^/watch/tenant_name"),
]
