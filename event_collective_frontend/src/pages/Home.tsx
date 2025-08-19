export default function Home() {
  return (
    <section className="space-y-6">
      <h1 className="text-3xl font-bold">Welcome to Event Collective</h1>
      <p className="text-gray-700 max-w-2xl">
        A modern event management studio. Explore our gallery, services, and reviews —
        or sign in to view your dashboard.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-6 rounded-2xl border shadow-sm">
          <h3 className="font-semibold text-lg">Gallery</h3>
          <p className="text-gray-600">See highlights from past events.</p>
        </div>
        <div className="p-6 rounded-2xl border shadow-sm">
          <h3 className="font-semibold text-lg">Services</h3>
          <p className="text-gray-600">Browse packages and pricing ranges.</p>
        </div>
        <div className="p-6 rounded-2xl border shadow-sm">
          <h3 className="font-semibold text-lg">Reviews</h3>
          <p className="text-gray-600">Read testimonials from clients.</p>
        </div>
      </div>
    </section>
  );
}
