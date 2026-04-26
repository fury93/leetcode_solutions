class Solution:

    class TrieNode:
        def __init__(self):
            self.is_end_of_folder = False
            self.children = {}

    def __init__(self):
        self.root = self.TrieNode()

    def removeSubfolders(self, folder):
        # Build Trie from folder paths
        for path in folder:
            current_node = self.root
            folders = path.split("/")

            for folder_name in folders:
                if folder_name == "":
                    continue

                # Create new node if it doesn't exist
                if folder_name not in current_node.children:
                    current_node.children[folder_name] = self.TrieNode()
                current_node = current_node.children[folder_name]

            # Mark the end of the folder path
            current_node.is_end_of_folder = True

        # Check each path for subfolders
        result = []
        for path in folder:
            current_node = self.root
            folders = path.split("/")
            is_subfolder = False

            for i, folder_name in enumerate(folders):
                if folder_name == "":
                    continue
                next_node = current_node.children[folder_name]
                # Check if the current folder path is a subfolder of an existing folder
                if next_node.is_end_of_folder and i != len(folders) - 1:
                    is_subfolder = True
                    break  # Found a subfolder
                current_node = next_node

            # If not a subfolder, add to the result
            if not is_subfolder:
                result.append(path)

        return result