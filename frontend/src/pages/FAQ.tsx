import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

const FAQ = () => {
  const faqs = [
    {
      question: "How do I enroll in a course?",
      answer: "Simply browse our course catalog, click on a course you're interested in, and click the 'Enroll Now' button. You'll need to create an account or log in to complete the enrollment process."
    },
    {
      question: "Are the certificates recognized?",
      answer: "Yes! Our certificate courses provide industry-recognized certificates upon completion. These certificates demonstrate your competency in the subject matter and can be shared on professional networks like LinkedIn."
    },
    {
      question: "Can I access courses on mobile devices?",
      answer: "Absolutely! Our platform is fully responsive and works seamlessly on all devices including smartphones, tablets, and desktop computers."
    },
    {
      question: "What's the difference between free and certificate courses?",
      answer: "Free courses provide introductory or beginner-level content and also include a certificate of completion. Certificate courses are more comprehensive, in-depth programs that provide advanced knowledge and industry-recognized certification."
    },
    {
      question: "How long do I have access to a course?",
      answer: "Once you enroll in a course, you have lifetime access to all course materials. You can learn at your own pace and revisit the content anytime."
    },
    {
      question: "Do you offer refunds?",
      answer: "Yes, we offer a 30-day money-back guarantee on all paid courses. If you're not satisfied with a course, contact our support team within 30 days of purchase for a full refund."
    },
    {
      question: "How do I contact support?",
      answer: "You can reach our support team at support@root.com or through our general contact at contact@root.com. We typically respond within 24 hours."
    },
    {
      question: "Can I download course materials?",
      answer: "Yes, most courses include downloadable resources such as PDFs, worksheets, and supplementary materials that you can keep forever."
    }
  ];

  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main className="py-20">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h1 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
              Frequently Asked <span className="text-primary">Questions</span>
            </h1>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Find answers to common questions about our platform and courses
            </p>
          </div>

          <div className="max-w-3xl mx-auto">
            <Accordion type="single" collapsible className="w-full">
              {faqs.map((faq, index) => (
                <AccordionItem key={index} value={`item-${index}`}>
                  <AccordionTrigger className="text-left">
                    {faq.question}
                  </AccordionTrigger>
                  <AccordionContent className="text-muted-foreground">
                    {faq.answer}
                  </AccordionContent>
                </AccordionItem>
              ))}
            </Accordion>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default FAQ;
