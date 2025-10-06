export type HomePayload = {
  settings: {
    brand_palette: string; hero_title: string; hero_subtitle: string;
    cta_text: string; cta_href: string; fb_url: string; ig_url: string; tiktok_url: string;
  } | null;
  nav: { label: string; href: string }[];
  services: { id:number; name:string; description?:string; price?:number|null; category?:string|null }[];
  gallery: { id:number; filename:string; url:string; alt_text?:string|null }[];
  reviews: { id:number; name:string; rating:number; message:string }[];
};

export async function fetchHome(): Promise<HomePayload> {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/public/home`, { credentials: "include" });
  if (!res.ok) throw new Error("Failed to load home");
  return res.json();
}
