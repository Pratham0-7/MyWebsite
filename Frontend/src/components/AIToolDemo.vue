<template>
  <div class="ai-tool-demo">
    <!-- Back Button -->
    <div class="back-button" @click="$router.back()">←</div>

    <!-- Hero Section -->
    <section class="hero"
     style="background: url('https://images.unsplash.com/photo-1530819568329-97653eafbbfa?q=80&w=1465&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center / cover"
    >
      <h1 class="hero-title">Welcome to SmartWriter</h1>
      <p class="hero-subtext">An AI tool that turns your raw thoughts into ready-to-post content.</p>
      <a href="#try" class="hero-button">Try Now</a>
    </section>

    <!-- How It Works -->
    <section class="section light">
      <h2 class="section-title">How It Works</h2>
      <div class="feature-grid">
        <div class="feature-box">
          <h3>1. Input Idea</h3>
          <p>Type your raw thought or topic in plain language.</p>
        </div>
        <div class="feature-box">
          <h3>2. Hit Generate</h3>
          <p>SmartWriter uses AI to generate clean, creative text.</p>
        </div>
        <div class="feature-box">
          <h3>3. Copy or Tweak</h3>
          <p>Copy the result instantly or make minor changes before using.</p>
        </div>
      </div>
    </section>

    <!-- Use Cases -->
    <section class="section">
      <h2 class="section-title">Perfect For</h2>
      <div class="tag-grid">
        <span class="tag">Social Media Captions</span>
        <span class="tag">Blog Intros</span>
        <span class="tag">Email Replies</span>
        <span class="tag">Cold DMs</span>
        <span class="tag">Product Descriptions</span>
        <span class="tag">YouTube Descriptions</span>
      </div>
    </section>

    <!-- Try It Out -->
    <section id="try" class="section light"
    style="background: url('https://images.unsplash.com/photo-1617791160536-598cf32026fb?q=80&w=1064&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center / cover"
    >
      <h2 class="section-title">Try It Now</h2>
      <p class="section-subtext">This is a demo preview. Real product will include login, history, and export features.</p>

      <div class="generate-box">
        <textarea v-model="inputText" placeholder="Type your idea here..." class="input-box"></textarea>
        <button class="hero-button" @click="generateContent">Generate</button>
      </div>

      <div v-if="outputText" class="output-box">
        <h3>Generated Output:</h3>
        <p>{{ outputText }}</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'AIToolDemo',
  data() {
    return {
      inputText: '',
      outputText: ''
    };
  },
  methods: {
    async generateContent() {
      if (!this.inputText) return;

      const res = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: this.inputText })
      });

      const data = await res.json();
      this.outputText = data.response || "Something went wrong.";
    }
  }
};
</script>

<style scoped>
.ai-tool-demo {
  font-family: sans-serif;
  background: #f9f9f9;
  color: #111;
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
  z-index: 1000;
}

.hero {
  text-align: center;
  padding: 100px 20px;
  background: #e0f2fe;
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
  background: #111;
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
  margin-bottom: 10px;
}

.section-subtext {
  max-width: 600px;
  margin: 0 auto 20px;
  font-size: 16px;
  color: black;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.feature-box {
  background: #f0f9ff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
}

.tag-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  justify-items: center;
  margin-top: 20px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.tag {
  background: #e2e8f0;
  padding: 8px 16px;
  border-radius: 999px;
  font-size: 14px;
  text-align: center;
}

.generate-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  margin-top: 20px;
}

.input-box {
  width: 100%;
  max-width: 700px;
  height: 120px;
  padding: 12px;
  font-size: 15px;
  border-radius: 8px;
  border: 1px solid #ccc;
}

.output-box {
  margin-top: 30px;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  background: #f3f4f6;
  padding: 16px;
  border-radius: 8px;
  text-align: left;
  box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
