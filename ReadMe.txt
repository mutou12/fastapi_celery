1、在机器中启动redis，一般是docker，启动命令如下：
docker run --name myredis -d -p 6379:6379 redis
2、在目录文件夹下启动，后台程序就可以启动起来了
uvicorn main:app --reload