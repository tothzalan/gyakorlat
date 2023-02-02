
const dummyData = { 'companies': [
    { 'name': 'TesztSoft', 'url': 'https://google.com', technologies: [ 'Go', 'C++'] },
    { 'name': 'MasikSoft', 'url': 'https://facebook.com', technologies: [ 'PHP', 'React'] },
]}

const container = document.getElementById('container')

dummyData.companies.map(comp => {
    const div = document.createElement('div')

    const a = document.createElement('a')
    a.innerText = comp.name
    a.href = comp.url
    a.target = '_blank'
    div.appendChild(a)

    const p = document.createElement('p')
    comp.technologies.forEach(t => {
        p.innerText += `${t} `
    })
    div.appendChild(p)

    container.appendChild(div)
})
