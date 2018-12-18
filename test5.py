#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import random
import websockets

async def oogiri(websocket, path):
    while True:
        count = 0
        shota_1 = "昇太：山田くーん！座布団一枚持ってきて～！"
        yamada_1 = "山田：は～い！"
        zabuton_10 = "座布団10枚です！おめでとう！"
        shota_2 = "昇太：山田くーん、座布団みーんな持って行って〜！"
        yamada_2 = "山田：はい、かしこまりましたー！！"
        for i in range(10):
            count += 1
            zabuton_count = "＜座布団：" + str(count) + "枚＞"
            await websocket.send(shota_1)
            await asyncio.sleep(1)
            await websocket.send(yamada_1)
            await websocket.send(zabuton_count)
            await asyncio.sleep(random.random() * 3)
        await websocket.send(zabuton_10)
        await websocket.send(shota_2)
        await asyncio.sleep(1)
        await websocket.send(yamada_2)


start_server = websockets.serve(oogiri, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
