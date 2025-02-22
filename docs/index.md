---
title: Home
layout: page
---

<style>
    body {
        background: radial-gradient(circle at center, #000000, #1b0035, #3a005f);
        color: #e0e0e0;
    }

    .galaxy-header {
        font-size: 3.5rem;
        text-transform: uppercase;
        text-shadow: 0 0 25px #00ffcc, 0 0 40px #ff00ff;
        margin: 3rem 0;
        animation: title-glow 2s infinite alternate;
        letter-spacing: 0.2rem;
    }

    @keyframes title-glow {
        0% { text-shadow: 0 0 25px #00ffcc, 0 0 40px #ff00ff; }
        50% { text-shadow: 0 0 35px #00ffff, 0 0 50px #ff00ff; }
        100% { text-shadow: 0 0 25px #00ffcc, 0 0 40px #ff00ff; }
    }

    .cosmic-divider {
        height: 2px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            #ff00ff 30%, 
            #00ffff 70%, 
            transparent 100%);
        margin: 4rem auto;
        width: 80%;
        max-width: 800px;
        box-shadow: 0 0 15px #ff00ff55;
    }

    .stellar-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 4rem auto;
        max-width: 1200px;
        padding: 0 2rem;
    }

    .nebula-card {
        padding: 2rem;
        background: rgba(0, 0, 0, 0.25);
        border: 1px solid #ff00ff;
        border-radius: 12px;
        position: relative;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        overflow: hidden;
    }

    .nebula-card::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(45deg, 
            #ff00ff22 0%, 
            #00ffff22 50%, 
            #ff00ff22 100%);
        z-index: -1;
        animation: nebula-pulse 8s infinite linear;
    }

    @keyframes nebula-pulse {
        0% { opacity: 0.3; }
        50% { opacity: 0.1; }
        100% { opacity: 0.3; }
    }

    .nebula-card h3 {
        font-size: 1.8rem;
        color: #00ffff;
        text-shadow: 0 0 15px #00ffff;
        margin-bottom: 1.5rem;
        border-left: 3px solid #ff00ff;
        padding-left: 1rem;
    }

    .nebula-card ol {
        list-style: none;
        counter-reset: cosmic-counter;
        padding: 0;
    }

    .nebula-card li {
        counter-increment: cosmic-counter;
        margin: 1rem 0;
        padding: 0.8rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 6px;
        position: relative;
        transition: all 0.3s ease;
    }

    .nebula-card li::before {
        content: counter(cosmic-counter);
        color: #ff00ff;
        font-weight: bold;
        margin-right: 1rem;
        text-shadow: 0 0 10px #ff00ff;
    }

    .nebula-card li:hover {
        transform: translateX(10px);
        background: rgba(255, 255, 255, 0.1);
    }

    .launch-container {
        text-align: center;
        margin: 4rem 0;
    }

    .singularity-button {
        padding: 1.2rem 3rem;
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        border: none;
        border-radius: 8px;
        color: white;
        font-size: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 0.1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 25px #ff00ff;
        position: relative;
        overflow: hidden;
    }

    .singularity-button::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(45deg, 
            transparent 0%, 
            rgba(255,255,255,0.1) 50%, 
            transparent 100%);
        animation: button-glow 2s infinite;
    }

    @keyframes button-glow {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }

    .singularity-button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 40px #00ffff;
    }
</style>

<h1 class="galaxy-header">Astro Recognizer</h1>

<div class="cosmic-divider"></div>

<p style="text-align: center; font-size: 1.3rem; max-width: 800px; margin: 2rem auto; line-height: 1.6;">
    Deep space imaging system specialized in classifying 17 distinct categories of celestial objects and phenomena through advanced pattern recognition.
</p>

<div class="stellar-grid">
    <div class="nebula-card">
        <h3>Galactic Structures</h3>
        <ol>
            <li>Andromeda Galaxy</li>
            <li>Crab Nebula</li>
            <li>Eagle Nebula</li>
            <li>Milky Way Galaxy</li>
            <li>Orion Nebula</li>
            <li>Triangulum Galaxy</li>
        </ol>
    </div>

    <div class="nebula-card">
        <h3>Planetary Bodies</h3>
        <ol start="7">
            <li>Earth</li>
            <li>Jupiter</li>
            <li>Mars</li>
            <li>Mercury</li>
            <li>Neptune</li>
            <li>Saturn</li>
            <li>Uranus</li>
            <li>Venus</li>
        </ol>
    </div>

    <div class="nebula-card">
        <h3>Cosmic Phenomena</h3>
        <ol start="15">
            <li>Black Holes</li>
            <li>Exoplanets</li>
            <li>Supernova Remnants</li>
        </ol>
    </div>
</div>

<div class="cosmic-divider"></div>

<div class="launch-container">
    <a href="{{ site.baseurl }}/astro_recognizer" class="singularity-button">
        Begin Celestial Analysis
    </a>
</div>