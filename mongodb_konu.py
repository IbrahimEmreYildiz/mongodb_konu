import pymongo
from bson.objectid import ObjectId

myclient= pymongo.MongoClient('mongodb://localhost:27017')
mydb= myclient["node-app"]

print(myclient.list_database_names()) # Mevcut database'leri görüntüler


# UZAKTAKİ SERVER'A BAĞLANMA

myclient= pymongo.MongoClient('mongodb+srv://2020555069e:Tyildiz*20@cluster0.opbgw3p.mongodb.net/')
mydb= myclient['node-app'] # Database bağlanma
mycollection= mydb["products"] # Products collection'una gider. Eğer yoksa kendisi oluşturur
print(myclient.list_database_names()) # Database isimlerini listeleme
print(mydb.list_collection_names()) # Collection isimlerini listeler

product= {"name":"Samsung S5", "price": 2000}

result= mycollection.insert_one(product) #Eğer tek kayıt ekleyeceksek insert_one
print(result) # Bir InsertOne nesnesi gönderir çıktı olarak
print(type(result)) # Class'tır
print(result.inserted_id) #Eklenen kaydın id'sini gösterir.


productList= [
    {"name":"Samsung S12", "price": 3000, "description": "iyi telefon"},
    {"name":"Samsung S13", "price": 4000, "categories": ['telefon', 'elektrik']}

]

result= mycollection.insert_many(productList)# insert many çünkü birden çok kayıt ekliyoruz.
print(result.inserted_ids) #Inserted ids çünkü çok id gelecek.

#SELECT işlemi Select= mongodb'de find'dır

result= mycollection.find_one() #Bulduğu ilk kaydı getirir
print(result)

for i in mycollection.find({}, {"_id":0, "name":1, "price":1}): # eğer 0 verirsek çıktıda gözükmez 1 verirsek gözükür.
    print(i)
    print("\n")


for i in mycollection.find({}, {"_id":0, "name": 0}): # Eğer 1 olarak hiçbir şey yazmazsak 0 verdiğimiz hariç tüm bilgileri getirir
    print(i)
    print("\n")


for i in mycollection.find({}, {"name": 1}): # Eğer  id hakkında 0 yazmazsak o her türlü gelir.
    print(i)
    print("\n")


# Filtreleme işlemi

filter= {"name":"Samsung S5"}
result= mycollection.find(filter)

for i in result:
    print(i)

result= mycollection.find_one({"_id":ObjectId("69cac923b23db0f488d6d1a6")})
# Burada aslında o id'de bir kayıt var ama string olarak id değil de ObjectId nesnesi olarak geçiyor o yüzden import etmemiz lazım ve id numarasını object id nesenesi olarak aramalıyız.
print(result)


#MONGODB OPERATORLERİ OLARAK ARATIRSAN GOOGLE'DA VAR

result= mycollection.find({
    "name": {
        "$in": ["Samsung S5","Samsung S6"] #Bu $in mongodb'nin kendi özelliği
    }
})
for i in result:
    print(i)

result= mycollection.find({
    "price": {
        "$gt": 2000 # $gt greater than demek fiyatı 2000 den büyük kayıtları yazdır $gte yaparsak büyük eşit demektir.

    }
})
for i in result:
    print(i)

result= mycollection.find({
    "price": {
        "$eq": 3000 # $eq eşit olanları gösterir 
    }
})
for i in result:
    print(i)



result= mycollection.find({
    "name": { "$regex": "^S"} #regex de kullanabiliriz mesela S ile başlayan ifadeler demek bu


})
for i in result:
    print(i)


#Kayıtları sıralama


result= mycollection.find().sort('name',1) # Column'dan sonra 1 dersek artan -1 dersek azalan sıralama yapar

for i in result:
    print(i)
    print("\n")
    
result= mycollection.find().sort('price',-1) # Column'dan sonra 1 dersek artan -1 dersek azalan sıralama yapar

for i in result:
    print(i)
    print("\n")


#UPDATE METHODU

mycollection.update_one(   #update_one bulduğu ilk kaydı değiştirir önce değiştireceğimiz kaydı sonra $set komutu ile değişimi yazıyoruz
    {"name": "Samsung S5"},
    {"$set": {
        "name": "Iphone 6"
    }}
)

for i in mycollection.find():
    print(i)



mycollection.update_one(
    {"name": "Samsung S6"},
    {"$set": {
        "name": "Iphone 7"
    }}
)

for i in mycollection.find():
    print(i)

#update_many'nin kullanımı update_one ile aynı sadece birden çok aynı kayıt varsa update_many kullanılır


#DELETE METHODU

#delete_one() 1 kayıt delete_many() çok kayıt silmek için kullanılır




mycollection.delete_one({"name": "Samsung S10"})
mycollection.delete_many({"name": "Samsung S10"}) # Birden fazla aynı kayıt varsa onu silmek için kullanılır
mycollection.delete_many({"name": {"$regex": "^S"}}) 
mycollection.delete_many({}) # Böyle boş parantez koyarsak tüm kayıtlar silinir
for i in mycollection.find():
    print(i)


