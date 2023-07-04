import folium

m = folium.Map(location=[34.3481671,134.0515907],zoom_start=10)
m

folium.Marker(location=[34.3287807,134.091987],popup='エディオン 高松春日店　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.3151017,134.0417901],popup='エディオン ゆめタウン高松店　　　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.2743747,133.7840166],popup='エディオン ゆめタウン丸亀北店　　　　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.145182,133.698639],popup='エディオン ゆめタウン三豊店　　　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.2518415,133.9308102],popup='ヤマダデンキ テックランド綾川店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.1187562,133.6773401],popup='ヤマダデンキ テックランド観音寺店　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3324732,134.0101332],popup='ヤマダデンキ テックランド高松鶴市店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.2663845,133.7974991],popup='ヤマダデンキ テックランド丸亀店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3113665,134.0600482],popup='ヤマダデンキ テックランドNew高松レインボー通り店　　　　　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.2694501,134.1764377],popup='ヤマダデンキ ヤマダアウトレットさぬき長尾店　　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3200306,134.092099],popup='ヤマダデンキ Tecc LIFE SELECT 高松春日店　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.2513182,133.9354578],popup='ケーズデンキ 綾川店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.3083429,133.8098664],popup='ケーズデンキ イオンタウン宇多津店　　　　　　　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.1231527,133.6622149],popup='ケーズデンキ 観音寺店　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.1758337,133.7171486],popup='ケーズデンキ 高瀬店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.3178588,134.0928826],popup='ケーズデンキ 高松春日店　　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.2941842,134.0544123],popup='ケーズデンキ 高松本店　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.4885219,134.1927972],popup='ケーズデンキ 土庄店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.259773,133.7860445],popup='ケーズデンキ 丸亀店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.3518900,134.0052059],popup='イオンモバイル 高松店　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[34.3456152,134.0715872],popup='イオンモバイル 高松東店　　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[34.4882535,134.1867706],popup='マツヤデンキ 小豆島店　　　　　　　　　　',icon=folium.Icon(color="darkblue")).add_to(m)
m

folium.Marker(location=[34.3090244,134.0606214],popup='パソコン工房 高松店　　　　　　　　　',icon=folium.Icon(color="green")).add_to(m)
m

folium.Marker(location=[34.3481671,134.0515907],popup='マーキュリー 香川営業所　　　　　　　　　　　',icon=folium.Icon(color="white")).add_to(m)
m

m.save('kagawaken_kaden_mobile.html')
