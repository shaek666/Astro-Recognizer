---
title: Home
layout: page
---

<style>
    .cosmic-nav {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin: 3rem 0;
    }

    .cosmic-link {
        padding: 1rem 2rem;
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        border-radius: 8px;
        color: white!important;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 0 15px #ff00ff;
        animation: neonPulse 2s infinite alternate;
    }

    @keyframes neonPulse {
        0% { box-shadow: 0 0 15px #ff00ff; }
        100% { box-shadow: 0 0 30px #00ffff; }
    }

    .cosmic-link:hover {
        transform: scale(1.05);
        box-shadow: 0 0 40px #00ffff;
    }

    .elements-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 3rem auto;
        max-width: 1200px;
    }

    .cosmic-card {
        padding: 1.5rem;
        background: rgba(0, 0, 0, 0.3);
        border: 1px solid #ff00ff;
        border-radius: 10px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .cosmic-card::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(45deg, 
            transparent 0%, 
            #ff00ff22 30%, 
            #00ffff22 70%, 
            transparent 100%);
        z-index: -1;
    }

    .cosmic-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 30px #ff00ff55;
    }

    .galaxy-header {
        font-size: 2.5rem;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 0 0 15px #00ffcc, 0 0 30px #ff00ff;
        animation: glowPulse 2s infinite alternate;
    }

    @keyframes glowPulse {
        0% { text-shadow: 0 0 15px #00ffcc, 0 0 30px #ff00ff; }
        100% { text-shadow: 0 0 25px #00ffff, 0 0 40px #ff00ff; }
    }

    .quantum-divider {
        height: 2px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            #ff00ff 30%, 
            #00ffff 70%, 
            transparent 100%);
        margin: 3rem auto;
        width: 80%;
        max-width: 800px;
    }
</style>

<div class="cosmic-nav">
    <a href="{{ site.baseurl }}/" class="cosmic-link">🌌 Home</a>
    <a href="{{ site.baseurl }}/astro_recognizer" class="cosmic-link">🔭 Classifier</a>
</div>

<h1 class="galaxy-header">Astro Recognizer</h1>

<div class="quantum-divider"></div>

<p style="text-align: center; font-size: 1.2rem; max-width: 800px; margin: 2rem auto;">
    Advanced deep space pattern recognition system capable of classifying 17 distinct celestial phenomena with quantum-level accuracy.
</p>

<div class="elements-grid">
    <div class="cosmic-card">
        <h3>🌠 Galactic Structures</h3>
        <ol>
            <li>Andromeda Galaxy</li>
            <li>Crab Nebula</li>
            <li>Eagle Nebula</li>
            <li>Milky Way Galaxy</li>
            <li>Orion Nebula</li>
            <li>Triangulum Galaxy</li>
        </ol>
    </div>

    <div class="cosmic-card">
        <h3>🪐 Planetary Bodies</h3>
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

    <div class="cosmic-card">
        <h3>💫 Cosmic Phenomena</h3>
        <ol start="15">
            <li>Black Holes</li>
            <li>Exoplanets</li>
            <li>Supernova Remnants</li>
        </ol>
    </div>
</div>

<div class="quantum-divider"></div>

<div style="text-align: center; margin: 3rem 0;">
    <a href="{{ site.baseurl }}/astro_recognizer" class="cosmic-link" style="font-size: 1.5rem;">
        🚀 Launch Classifier
    </a>
</div>