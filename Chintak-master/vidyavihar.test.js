const { fireEvent, getByText } =  require('@testing-library/dom');

const { JSDOM } =  require('jsdom');
const fs =  require('fs');
const path =  require('path');








const html = fs.readFileSync(path.resolve(__dirname, './index.html'), 'utf8');

let dom
let container

describe('index.html', () => {
  beforeEach(() => {
    // Constructing a new JSDOM with this option is the key
    // to getting the code in the script tag to execute.
    // This is indeed dangerous and should only be done with trusted content.
    // https://github.com/jsdom/jsdom#executing-scripts
    dom = new JSDOM(html, { runScripts: 'dangerously' })
    container = dom.window.document.body
  })

  it('Null Checks of important Feilds', () => {
    expect(container.querySelector('h2')).not.toBeNull()
    expect(container.querySelector('p')).not.toBeNull()


  })
  
  it('Checks for working of Nav bar', () => {
    const delhilink = getByText(container, 'Delhi Region');
    const dharavilink = getByText(container, 'Dharavi Region');
    const Vidyaviharlink = getByText(container, 'Somaiya Vidyavihar');

    expect(delhilink).not.toBeNull();
    expect(dharavilink).not.toBeNull();
    expect(Vidyaviharlink).not.toBeNull();
    
  })

  it('Checking clickabilty of links', () => {
    const delhilink = getByText(container, 'Delhi Region');
    const dharavilink = getByText(container, 'Dharavi Region');
    const Vidyaviharlink = getByText(container, 'Somaiya Vidyavihar');

    fireEvent.click(delhilink);
    

    // setting timeout for page loading 
    setTimeout(function(){
        var currUrl = window.location.href;
        expect(currUrl).not.toBeNull();
        expect(currUrl).toEqual("https://kadam-tushar.github.io/Chintak/dharvi.html");
    },5000);
    
    fireEvent.click(dharavilink);

    setTimeout(function(){
        var currUrl = window.location.href;
        expect(currUrl).not.toBeNull();
        expect(currUrl).toEqual("https://kadam-tushar.github.io/Chintak/vidyavihar.html");
    },5000);


    fireEvent.click(Vidyaviharlink);

    setTimeout(function(){
        var currUrl = window.location.href;
        expect(currUrl).not.toBeNull();
        expect(currUrl).toEqual("https://kadam-tushar.github.io/Chintak/delhi.html");
    },5000);


    
    
  })

  



  




})