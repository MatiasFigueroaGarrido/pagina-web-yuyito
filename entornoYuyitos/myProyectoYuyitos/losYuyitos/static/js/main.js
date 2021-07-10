//$(function(){alert()});

// variables

let nav = document.getElementById('nav');
let menu = document.getElementById('enlaces');
let abrir = document.getElementById('open');
let botones = document.getElementsByClassName('btn-header');
let cerrado = true;

function menus(){
    let Desplazamiento_Actual = window.pageYOffset;

    if(Desplazamiento_Actual <= 300){
        nav.classList.remove('nav2');
        nav.className = ('nav1');
        nav.style.transition = '1s';
        menu.style.top = '80px';
        abrir.style.color = '#fff';
    }else{
        nav.classList.remove('nav1');
        nav.className = ('nav2');
        nav.style.transition = '1s';
        menu.style.top = '100px';
        abrir.style.color = '#000';
    }
};

function apertura(){
    if(cerrado){
        menu.style.width = '70vw';
        cerrado = false;
    }else{
        menu.style.width = '0%';
        menu.style.overflow = 'hidden';
        cerrado = true;
    }
};

window.addEventListener('load', function(){
    $('#onload').fadeOut();
    $('body').removeClass('hidden');
    menus()
});

window.addEventListener('click', function(e){
    //console.log(e.target);
    if(cerrado==false){
        let span = document.querySelector('span');
        if(e.target !== span && e.target !== abrir){
            menu.style.width = '0%';
            menu.style.overflow = 'hidden';
            cerrado = true;
        }
    }
});

window.addEventListener('scroll', function(){
    //console.log(window.pageYOffset);
    menus();
});

window.addEventListener('resize', function(){
    if(screen.width>= 700){
        cerrado = true;
        menu.style.removeProperty('overflow');
        menu.style.removeProperty('width');
    }
})

abrir.addEventListener('click', function(){
    apertura();
})


function HoverCarousel(elm, settings) {
    this.DOM = {
      scope: elm,
      wrap: elm.querySelector("ul").parentNode
    };
  
    this.containerWidth = 0;
    this.scrollWidth = 0;
    this.posFromLeft = 0; 
    this.stripePos = 0; 
    this.animated = null;
    this.callbacks = {};
  
    this.init();
  }
  
  HoverCarousel.prototype = {
    init() {
      this.bind();
    },
  
    destroy() {
      this.DOM.scope.removeEventListener(
        "mouseenter",
        this.callbacks.onMouseEnter
      );
      this.DOM.scope.removeEventListener("mousemove", this.callbacks.onMouseMove);
    },
  
    bind() {
      this.callbacks.onMouseEnter = this.onMouseEnter.bind(this);
      this.callbacks.onMouseMove = (e) => {
        if (this.mouseMoveRAF) cancelAnimationFrame(this.mouseMoveRAF);
  
        this.mouseMoveRAF = requestAnimationFrame(this.onMouseMove.bind(this, e));
      };
  
      this.DOM.scope.addEventListener("mouseenter", this.callbacks.onMouseEnter);
      this.DOM.scope.addEventListener("mousemove", this.callbacks.onMouseMove);
    },
  
    
    onMouseEnter(e) {
      this.nextMore = this.prevMore = false; 
  
      this.containerWidth = this.DOM.wrap.clientWidth;
      this.scrollWidth = this.DOM.wrap.scrollWidth;
      this.padding = 0.2 * this.containerWidth;
      this.posFromLeft = this.DOM.wrap.getBoundingClientRect().left;
      var stripePos = e.pageX - this.padding - this.posFromLeft;
      this.pos = stripePos / (this.containerWidth - this.padding * 2);
      this.scrollPos = (this.scrollWidth - this.containerWidth) * this.pos;
  
      this.DOM.wrap.style.scrollBehavior = "smooth";
  
      if (this.scrollPos < 0) this.scrollPos = 0;
  
      if (this.scrollPos > this.scrollWidth - this.containerWidth)
        this.scrollPos = this.scrollWidth - this.containerWidth;
  
      this.DOM.wrap.scrollLeft = this.scrollPos;
      this.DOM.scope.style.setProperty(
        "--scrollWidth",
        (this.containerWidth / this.scrollWidth) * 100 + "%"
      );
      this.DOM.scope.style.setProperty(
        "--scrollLleft",
        (this.scrollPos / this.scrollWidth) * 100 + "%"
      );
  
      clearTimeout(this.animated);
      this.animated = setTimeout(() => {
        this.animated = null;
        this.DOM.wrap.style.scrollBehavior = "auto";
      }, 200);
  
      return this;
    },
  
    onMouseMove(e) {
      if (this.animated) return;
  
      this.ratio = this.scrollWidth / this.containerWidth;
  
      var stripePos = e.pageX - this.padding - this.posFromLeft;
  
      if (stripePos < 0) stripePos = 0;
  
      this.pos = stripePos / (this.containerWidth - this.padding * 2);
  
      this.scrollPos = (this.scrollWidth - this.containerWidth) * this.pos;
  
      this.DOM.wrap.scrollLeft = this.scrollPos;
  
      if (this.scrollPos < this.scrollWidth - this.containerWidth)
        this.DOM.scope.style.setProperty(
          "--scrollLleft",
          (this.scrollPos / this.scrollWidth) * 100 + "%"
        );
  
      this.prevMore = this.DOM.wrap.scrollLeft > 0;
      this.nextMore =
        this.scrollWidth - this.containerWidth - this.DOM.wrap.scrollLeft > 5;
  
      this.DOM.scope.setAttribute(
        "data-at",
        (this.prevMore ? "left " : " ") + (this.nextMore ? "right" : "")
      );
    }
  };
  
  var carouselElm = document.querySelector(".carousel");
  new HoverCarousel(carouselElm);