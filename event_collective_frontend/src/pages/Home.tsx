import { useEffect, useState } from "react";
import LeftRailNav from "../components/LeftRailNav";
import Hero from "../components/Hero";
import AboutBlurb from "../components/AboutBlurb";
import FeatureCards from "../components/FeatureCards";
import GalleryMarquee from "../components/GalleryMarquee";
import SocialBar from "../components/SocialBar";
import { fetchHome, type HomePayload } from "../lib/api";

export default function Home() {
  const [data, setData] = useState<HomePayload | null>(null);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    fetchHome().then(setData).catch(e => setErr(String(e)));
  }, []);

  if (err) return <div className="pl-24 md:pl-32 py-10 text-red-500">Failed to load home: {err}</div>;
  if (!data) return <div className="pl-24 md:pl-32 py-10">Loading…</div>;

  const s = data.settings ?? {
    brand_palette: "offwhite_black",
    hero_title: "The Event Collective",
    hero_subtitle: "Modern, classy coordination & rentals.",
    cta_text: "Inquire",
    cta_href: "/contact",
    fb_url: "", ig_url: "", tiktok_url: ""
  };

  return (
    <div className="relative">
      <LeftRailNav items={data.nav} />
      <main className="ml-20 md:ml-28">
        <Hero title={s.hero_title} subtitle={s.hero_subtitle} ctaText={s.cta_text} ctaHref={s.cta_href} />
        <AboutBlurb />
        <FeatureCards services={data.services} />
        <GalleryMarquee images={data.gallery.map(g => ({ id:g.id, url:g.url, alt_text:g.alt_text }))} />
        <SocialBar fb={s.fb_url} ig={s.ig_url} tt={s.tiktok_url} />
      </main>
    </div>
  );
}
