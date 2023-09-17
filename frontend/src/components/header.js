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
  if(window.scrollY > 50) {
    setScrolled(true)
  } else {
    setScrolled(false)
  }
}
    return (
        <div>
            <div class={`App-header ${isScrolled && 'header-scrolled'}`}>
                <p><a href="/home">crescendo</a></p>
                {/* <div class="App-logo">
                  {!isScrolled && (
                    <img src="./sheep_new.png" alt="Crescendo Sheep Logo" class="logo"/>
                  )}
                </div> */}
            </div>
        </div>
    );
}

export default Header;