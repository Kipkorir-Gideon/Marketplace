const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['your-image-domain.com'], // Replace with your image domain
  },
  env: {
    API_URL: process.env.API_URL || 'http://localhost:5000', // Set your API URL
  },
};

module.exports = nextConfig;