/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./ecommerce_app/templates/**/*.{html,js}", // HTML veya JavaScript dosyalarını izler
    "./ecommerce_app/static/**/*.css", // ecommerce_app içindeki tüm statik CSS dosyalarını izler
    "./node_modules/flowbite/**/*.js", // Flowbite modülünü izler
    "./ecommerce_app/products/forms.py", // Django form dosyasını izler
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
