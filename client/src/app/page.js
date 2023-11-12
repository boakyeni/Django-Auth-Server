import Image from 'next/image'
import Link from 'next/link'
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Link href="http://localhost:8080/dashboard">dashboard</Link>
      <Link href="http://localhost:8080/o/authorize/?response_type=code&code_challenge=w-RNB5C4H51ccZ5JjmonjIECAMxxSmZVB4wOTUhDTp8&code_challenge_method=S256&client_id=uP2K3DvVVNK1jex03QfL1kuwWy8ub8AegMHUAQaC&redirect_uri=http://localhost:8080/dashboard">login</Link>
    </main>
  )
}
