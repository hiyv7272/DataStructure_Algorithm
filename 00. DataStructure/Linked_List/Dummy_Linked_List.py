class Node:

	def __init__(self, item):
		self.data = item
		self.next = None


class LinkedList:
	def __init__(self):
			self.nodeCount = 0
			self.head = Node(None)
			self.tail = None
			self.head.next = self.tail


	def __repr__(self):
		if self.nodeCount == 0:
			return 'LinkedList: empty'

		s = ''
		curr = self.head
		while curr.next:
			curr = curr.next
			s += repr(curr.data)
			if curr.next is not None:
				s += ' -> '
		return s


	def getLength(self):
		return self.nodeCount


	def traverse(self):
		result = []
		curr = self.head
		while curr.next:
			curr = curr.next
			result.append(curr.data)
		return result


	def getAt(self, pos):
		if pos < 0 or pos > self.nodeCount:
			return None

		i = 0
		curr = self.head
		while i < pos:
			curr = curr.next
			i += 1

		return curr


	def insertAfter(self, prev, newNode):
		newNode.next = prev.next
		if prev.next is None:
			self.tail = newNode
		prev.next = newNode
		self.nodeCount += 1
		return True


	def insertAt(self, pos, newNode):
		if pos < 1 or pos > self.nodeCount + 1:
			return False

		if pos != 1 and pos == self.nodeCount + 1:
			prev = self.tail
		else:
			prev = self.getAt(pos - 1)
		return self.insertAfter(prev, newNode)


	def popAfter(self, prev):
		# 삭제하려는 노드를 curr에 담기
		curr = prev.next

		# prev다음에 노드가 없는 경우 삭제할 노드가 없으니 None 리턴
		if prev.next == None:
		return None

		# 삭제할 노드가 없는 경우
		if curr.next == None:
		# 유일한 노드일 때
		if self.nodeCount == 1:
				self.tail = None
		# 유일한 노드가 아닐 때
		else:
			self.tail = prev

		# 링크 조정
		prev.next = curr.next
		self.nodeCount -= 1

		return curr.data


	def popAt(self, pos):
		if pos < 1 or pos > self.nodeCount:
		raise IndexError

		prev = self.getAt(pos - 1)

		return self.popAfter(prev)


	def concat(self, L):
		self.tail.next = L.head.next
		if L.tail:
			self.tail = L.tail
		self.nodeCount += L.nodeCount
