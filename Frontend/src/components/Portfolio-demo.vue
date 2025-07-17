<template>
  <div class="portfolio-demo">
    <!-- Back Button -->
    <div class="back-button" @click="$router.back()">
      ←
    </div>

    <!-- Hero Section -->
    <section class="hero"
      style="background: url('https://images.unsplash.com/photo-1604964432806-254d07c11f32?q=80&w=1600&auto=format&fit=crop') no-repeat center center / cover;"
    >
      <h1 class="hero-title">Hi, I’m [Your Name]</h1>
      <p class="hero-subtext">Full-Stack Developer • AI Engineer • Problem Solver</p>
      <a href="#contact" class="hero-button">Let’s Work Together</a>
    </section>

    <!-- About Section -->
    <section class="section light">
      <h2 class="section-title">About Me</h2>
      <p class="section-subtext">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla harum incidunt nostrum ducimus dolores rerum quam tempore ipsum tempora sequi eum dolor porro, rem nemo eveniet. Enim, architecto cumque similique tempore nemo, magni inventore ratione quis labore ducimus exercitationem, voluptas praesentium? Quam, corporis? Accusamus iusto soluta praesentium voluptas, ipsam maxime.
      </p>
    </section>

    <!-- Skills Section -->
    <section class="section"
    style="background: url('https://images.unsplash.com/photo-1510674485131-dc88d96369b4?q=80&w=649&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center / cover"
    >
      <h2 class="section-title">Tech I Use</h2>
      <div class="grid-4">
        <span class="tag">Vue.js</span>
        <span class="tag">React</span>
        <span class="tag">Node.js</span>
        <span class="tag">Python</span>
        <span class="tag">GPT APIs</span>
        <span class="tag">MongoDB</span>
        <span class="tag">Tailwind</span>
        <span class="tag">Vercel</span>
      </div>
    </section>

    <!-- Projects Section -->
    <section class="section light">
      <h2 class="section-title">Sample Projects</h2>
      <div class="project-grid-2">
        <div class="project-card square">
          <h3>Project 1: Insight AI</h3>
          <p>A tool that summarizes lengthy reports using GPT-4. Users paste content, click a button, and get sharp summaries instantly.</p>
        </div>
        <div class="project-card square">
          <h3>Project 2: OnePage Resume</h3>
          <p>A single-page resume site builder for professionals. Inputs your details and generates a shareable, styled webpage in seconds.</p>
        </div>
        <div class="project-card square">
          <h3>Project 3: SnapForm</h3>
          <p>A form-builder tool with GPT-enhanced auto-suggestions. Great for client onboarding or collecting leads with speed.</p>
        </div>
        <div class="project-card square">
          <h3>Project 4: FitTrack</h3>
          <p>Minimal fitness goal tracker with reminders and progress charts. Built for mobile-first usage and ultra-fast loading.</p>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section"
    style="background: url('https://images.unsplash.com/photo-1613993995046-07bce4b0bfed?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center / cover"
    >
      <h2 class="section-title">Let’s Connect</h2>
      <p class="section-subtext">Email me, call me, or WhatsApp me. I’m always open to building cool stuff.</p>
      <div class="contact-info">
        <p>📞 <strong>[Your Phone Number]</strong></p>
        <p>📧 <strong>[Your Email]</strong></p>
        <p>💬 <strong>WhatsApp Same As Phone</strong></p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'PortfolioDemo',
};
</script>

<style scoped>
.portfolio-demo {
  font-family: sans-serif;
  color: #111;
  background: #f8f8f8;
  position: relative;
}
.back-button {
  position: fixed;
  top: 20px;
  left: 20px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #e5e7eb;
  color: #111;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  cursor: pointer;
  transition: background 0.3s;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}
.back-button:hover {
  background: #d1d5db;
}
.hero {
  text-align: center;
  padding: 80px 20px;
  background: #fff;
  animation: fadeIn 1s ease-out;
}
.hero-title {
  font-size: 36px;
  font-weight: bold;
}
.hero-subtext {
  font-size: 18px;
  color: whitesmoke;
  margin: 12px 0 24px;
}
.hero-button {
  background: #000;
  color: #fff;
  padding: 12px 28px;
  border-radius: 8px;
  text-decoration: none;
  display: inline-block;
  transition: 0.3s;
}
.hero-button:hover {
  opacity: 0.85;
}
.section {
  padding: 60px 20px;
  text-align: center;
}
.section.light {
  background: #fff;
}
.section-title {
  font-size: 26px;
  font-weight: 600;
  margin-bottom: 16px;
}
.section-subtext {
  max-width: 700px;
  margin: 0 auto;
  font-size: 16px;
  color: #333;
}
.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  justify-items: center;
  margin-top: 20px;
}
.tag {
  background: #e2e8f0;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 14px;
  text-align: center;
  min-width: 100px;
}
.project-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 20px;
}
.project-card.square {
  background: #f1f5f9;
  padding: 10px;
  border-radius: 10px;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  text-align: left;
}
.contact-info {
  margin-top: 20px;
  font-size: 16px;
  color: #333;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
