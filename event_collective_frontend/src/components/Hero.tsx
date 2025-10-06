export default function Hero({title, subtitle, ctaText, ctaHref}:{title:string; subtitle:string; ctaText:string; ctaHref:string}) {
  return (
    <section className="min-h-[52vh] flex flex-col justify-center pl-24 pr-6 md:pl-32">
      <h1 className="text-4xl md:text-6xl font-light tracking-wide">{title}</h1>
      <p className="mt-4 max-w-xl text-base md:text-lg opacity-80">{subtitle}</p>
      <a href={ctaHref} className="mt-8 inline-block rounded-full px-6 py-3 border border-current hover:opacity-90">
        {ctaText}
      </a>
    </section>
  );
}
