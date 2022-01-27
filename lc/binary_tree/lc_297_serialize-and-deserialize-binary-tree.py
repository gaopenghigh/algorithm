# 297. 二叉树的序列化与反序列化
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# 使用前序遍历或后序遍历即可完成序列化，在序列化时将 None 也序列化为某个特殊字符，就可以实现反序列化。
# 中序不行，因为无法确定 root 在什么位置

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        buf = []
        self._serialize(root, buf)
        return ','.join(buf)
    
    def _serialize(self, root, buf):
        if root is None:
            buf.append('#')
            return
        buf.append(str(root.val))
        self._serialize(root.left, buf)
        self._serialize(root.right, buf)
        return buf
        

    def deserialize(self, data):
        data_list = data.split(',')
        return self._deserialize(data_list)
    
    def _deserialize(self, data_list):
        if not data_list:
            return None
        root_val = data_list.pop(0)
        if root_val == '#':
            return None
        root = TreeNode(int(root_val))
        root.left = self._deserialize(data_list)
        root.right = self._deserialize(data_list)
        return root


        

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Codec().serialize(root)
    print(s)
    newRoot = Codec().deserialize(s)
    print(Codec().serialize(newRoot))