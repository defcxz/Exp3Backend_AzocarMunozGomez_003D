var query = ''
var URL = ''
document.getElementById('enter').onclick = function(){
    query = document.getElementById('searchbar').value
    document.getElementById('searchbar').value = ''
    URL = 'https://www.googleapis.com/books/v1/volumes?q='+query

    clearPrevious();
    $.ajax({
      url: URL.toString(),
      dataType: 'json',
      success: function(data){
      console.log(data);

        for(i=0; i<10; i++){

            var booki = 'book'+(i+1)

            //crea las filas y las imagenes
            
            var imgRow = document.createElement('div')
            imgRow.className = "row imgRow"
            document.getElementById(booki).appendChild(imgRow)

            //titulo y precio de cada libro
            var titlePriceRow = document.createElement('div')
            titlePriceRow.className = "row titlePriceRow"
                
                var titleDiv = document.createElement('div')
                titleDiv.className = "col-md-8 title"
                titlePriceRow.appendChild(titleDiv)
                
                var priceDiv = document.createElement('div')
                priceDiv.className = "col-md-2 col-md-offset-1 price"
                titlePriceRow.appendChild(priceDiv)

                document.getElementById(booki).appendChild(titlePriceRow)

            //La  fila del autor
            var authorRow = document.createElement('div')
            authorRow.className = "row authorRow"
               
                var authorDiv = document.createElement('div')
                authorDiv.className = "col-md-12 author"
                authorRow.appendChild(authorDiv)

                document.getElementById(booki).appendChild(authorRow)

            //la fila de la descripcion 
            var descriptionRow = document.createElement('div')
            descriptionRow.className = "row descriptionRow"
               
                var descriptionDiv = document.createElement('div')
                descriptionDiv.className = "col-md-12 description"
                descriptionRow.appendChild(descriptionDiv)

                document.getElementById(booki).appendChild(descriptionRow)

            
            var img = document.createElement('img')
            img.src = data.items[i].volumeInfo.imageLinks.smallThumbnail
            document.getElementsByClassName('imgRow')[i].appendChild(img)

            
            var title = document.createElement('h1')
            title.innerHTML =  data.items[i].volumeInfo.title
            document.getElementsByClassName('title')[i].appendChild(title)

            //el precio de la informacion
            var price = document.createElement('h1')
            if(data.items[i].saleInfo.listPrice!=undefined){
                price.innerHTML = '$' + data.items[i].saleInfo.listPrice.amount
            }else{
                price.innerHTML = "N/A"
            }
            document.getElementsByClassName('price')[i].appendChild(price)

            //informacion del autor
            var author = document.createElement('p')
            author.innerHTML = 'By: ' +  data.items[i].volumeInfo.authors[0]
            document.getElementsByClassName('author')[i].appendChild(author)

            //informacion de la descripcion
            var description = document.createElement('p')
            description.innerHTML =  data.items[i].volumeInfo.description
            document.getElementsByClassName('description')[i].appendChild(description)

        }
      }
    })
}
//funcion para limpiar las filas
function clearPrevious(){
    for(i=0; i<10; i++){
        var booki = 'book'+(i+1)
        
       
        removeElementsByClass('imgRow')

        
        removeElementsByClass('titlePriceRow')   

        
        removeElementsByClass('authorRow')   

       
        removeElementsByClass('descriptionRow')
  
    }
}

function removeElementsByClass(className){
    var elements = document.getElementsByClassName(className);
    for(j=0; j<elements.length; j++){
        elements[0].parentNode.removeChild(elements[0]);
    }
}
