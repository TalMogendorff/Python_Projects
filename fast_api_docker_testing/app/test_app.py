import pytest
import os
import requests

@pytest.fixture(autouse=True, scope="module")
def docker_init_module():
    print("\n Docker is init")

    try:
        os.system(f'docker build -t testing-container-api ../')
        os.system(f"docker run -d -p 8000:8000 --name testing-container-api testing-container-api")
        print("\n python-fastapi Docker Run Succesfully")
        yield
        print("\n python-fastapi Docker ending proccess")
        os.system(f"docker stop testing-container-api")
        os.system(f"docker rm testing-con tainer-api")

    except:
        raise Exception



# @pytest.fixture(autouse=True,scope="function")
# def testing_printing():
#    try:
#       print("\n Docker is trying to run")
#
#       print("\n Docker is Running, starting test")
#    except:
#       raise Exception
#    finally:
#       print("\n testing is END, docker is closing.")

def test_api_1():
   print("Starting to test1")
   response = requests.get("http://127.0.0.1:8000")
   print(response.status_code)
   assert response.status_code == 200

def test_api_2():
   r = requests.get("http://127.0.0.1:8000")
   r.raise_for_status()

   print(str(r.json()["Hello"]))

def test_api_3():
   url = "http://127.0.0.1:8000/items"
   dynamic_id_flag = 1

   for dynamic_id_flag in range(5):
      r = requests.get(url+f"/{dynamic_id_flag}")
      dynamic_id_flag += 1
      print(r.json())

# def test_api_4():
#    url = "http://127.0.0.1:8000/items"
#    data = {"item_id": 35, "q": ""}
#    r = requests.put(url+"/0", data=data)
#
#    print(r.json())