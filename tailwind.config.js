// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.{html,js}", // Tüm HTML ve JavaScript dosyalarını izle
    "./static/**/*.css", // Tüm CSS dosyalarını izle
    "./node_modules/flowbite/**/*.js", // Flowbite modülünü izle
    "./**/*.py", // Proje genelindeki Python dosyalarını izle
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin"), // Flowbite plugin'i ekle
  ],
};
