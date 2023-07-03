import MainLayout from "@layouts/MainLayout";
import EditFreePost from "@scenes/Posts/EditPost/EditFreePost";
import { useRouter } from "next/router";

export default function UpdateFreePostPage() {
  const router = useRouter();
  const { id } = router.query;

  if (typeof id === "string") {
    return (
      <MainLayout>
        <EditFreePost id={id} />
      </MainLayout>
    );
  }
}
