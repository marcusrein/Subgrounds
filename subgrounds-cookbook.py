from subgrounds import Subgrounds

sg = Subgrounds.from_pg_key("pg-QIKcjxOnOo6bp4ZhgiMwttG7hyBePljY")

deployment_id = "QmQBvtHaTS9MftEWYTSmbbmPqzXtMpgZRidivvEaELSKsc"

seaport = sg.load_subgraph(
    f"https://api.playgrounds.network/v1/proxy/deployments/id/{deployment_id}"
)

top_collections = seaport.Query.collections(
    first=1001,
    orderBy=seaport.Collection.totalRevenueETH,
    orderDirection='desc',
)

query = sg.query_df([
    top_collections.name,
    top_collections.symbol,
    top_collections.totalRevenueETH,
    top_collections.creatorRevenueETH,
    top_collections.marketplaceRevenueETH],
    columns=['name', 'symbol', 'totalRevenueETH', 'creatorRevenueETH', 'marketplaceRevenueETH']
)

print(query)
