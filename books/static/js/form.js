
function styleForm() {
    let title = document.getElementById('id_title')
    title.classList.add('form-control')
    title.placeholder = 'informe o título'

    let isbn = document.getElementById('id_isbn')
    isbn.classList.add('form-control')
    isbn.placeholder = 'informe o ISBN'


    let author = document.getElementById('id_author')
    author.classList.add('form-control')


    let description = document.getElementById('id_description')
    description.classList.add('form-control')
    description.placeholder = 'Descrição'

    let launch = document.getElementById('id_launch')
    launch.classList.add('form-control')
    launch.placeholder = 'data de lançamento'

    let genre = document.getElementById('id_genre')
    genre.classList.add('form-control')
    genre.placeholder = 'informe o gênero textual'


    let category = document.getElementById('id_category')
    category.classList.add('form-control')
    category.placeholder = 'selecione a categoria'


    let edition = document.getElementById('id_edition')
    edition.classList.add('form-control')
    edition.placeholder = 'Informe a edição'

    let publisher = document.getElementById('id_publisher')
    publisher.classList.add('form-control')
    publisher.placeholder = 'Informe a editora'

    let price = document.getElementById('id_price')
    price.classList.add('form-control')

}

