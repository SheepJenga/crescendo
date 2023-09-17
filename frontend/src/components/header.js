import React, { useEffect, useState } from 'react'

function Header() {
  const [isScrolled, setScrolled] = useState(false);
  useEffect(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });

    return () => {
        window.removeEventListener('scroll', handleScroll);
    };
}, []);
const handleScroll = () => {
  if(window.scrollY > 100) {
    setScrolled(true)
  } else {
    setScrolled(false)
  }
}
    return (
        <div>
            <div class={`App-header ${isScrolled && 'header-scrolled'}`}>
                <h1>Crescendo</h1>
                <div class="App-logo">
                  {!isScrolled && (
                    <img src="./sheep_new.png" alt="Crescendo Sheep Logo" class="logo"/>
                  )}
                </div>
            </div>
        </div>
    );
}

export default Header;