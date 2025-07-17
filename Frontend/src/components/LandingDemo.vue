<template>
  <div class="landing-demo">
    <!-- Back Button -->
    <div class="back-button" @click="$router.back()">←</div>

    <!-- Hero Section -->
    <section class="hero"
    style="background: url('https://plus.unsplash.com/premium_photo-1675237625862-d982e7f44696?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center / cover"
    >
      <h1 class="hero-title">Welcome to Glow Coffee</h1>
      <p class="hero-subtext">Handcrafted coffee for bold mornings and calm nights.</p>
      <a href="#order" class="hero-button">Order Now</a>
    </section>

    <!-- Features Section -->
    <section class="section light">
      <h2 class="section-title">Why Choose Us?</h2>
      <div class="feature-grid">
        <div class="feature-box">
          <h3>✨ Fresh Beans</h3>
          <p>We roast small batches weekly to ensure peak flavor in every cup.</p>
        </div>
        <div class="feature-box">
          <h3>🌱 Sustainable</h3>
          <p>Eco-friendly packaging & ethical sourcing for a cleaner planet.</p>
        </div>
        <div class="feature-box">
          <h3>🚀 Fast Delivery</h3>
          <p>Your coffee delivered hot or cold in under 30 minutes.</p>
        </div>
      </div>
    </section>

    <!-- CTA / Pricing -->
    <section class="section">
      <h2 class="section-title">Plans & Pricing</h2>
      <p class="section-subtext">Try once, or subscribe for savings.</p>
      <div class="pricing-grid">
        <div class="price-card"
        style="background: url('https://plus.unsplash.com/premium_photo-1673459683873-a8a47e1a5ab9?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center / cover"
        >
          <h3 class="coffe-text">Single Cup</h3>
          <p class="coffee-price">₹199</p>
          <p class="coffee-sub">Try it now, no commitments.</p>
        </div>
        <div class="price-card"
          style="background: url('https://plus.unsplash.com/premium_photo-1681711650396-c4ba5767de04?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center / cover"
        >
        >
          <h3 class="coffee-text">Monthly Plan</h3>
          <p class="coffee-price">₹2,999</p>
          <p class="coffee-sub">Get 1 coffee delivered daily. Cancel anytime.</p>
        </div>
      </div>
    </section>

    <!-- Contact / Order Section -->
    <section id="order" class="section light"
    style="background: url('https://images.unsplash.com/photo-1498804103079-a6351b050096?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center / cover"
    >
      <h2 class="section-title wantacup">Want a Cup?</h2>
      <p class="section-subtext wantacupsubtext">Text us, WhatsApp us, or just click below.</p>
      <a href="https://wa.me/your-number" class="hero-button">Order via WhatsApp</a>
    </section>
  </div>
</template>

<script>
export default {
  name: 'LandingDemo'
};
</script>

<style scoped>
.landing-demo {
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
  background: #fff7ed;
  animation: fadeIn 1s ease-out;
}
.hero-title {
  font-size: 38px;
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
.wantacup{
    color: white;
}
.section-title {
  font-size: 26px;
  margin-bottom: 10px;
}
.section-subtext {
  max-width: 600px;
  margin: 0 auto 20px;
  font-size: 16px;
  color: #333;
}
.wantacupsubtext{
    color: whitesmoke;
}
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  margin-top: 30px;
}
.feature-box {
  background: #fefce8;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
}
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 30px;
}
.price-card {
  background: #fff;
  padding: 20px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
