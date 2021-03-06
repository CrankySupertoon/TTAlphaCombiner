from .bam.BamFile import BamFile

"""
  TOONTOWN ALPHA COMBINER
  First written for use in PANDORA

  Author: Disyer
  Date: 2020/06/13
"""
class CombinerBamFile(BamFile):

    def switch_texture_mode(self, convert_jpg, convert_rgb):
        target_ids = self.find_related('Texture')
        
        if not target_ids:
            # This model has no textures.
            return []

        modified_textures = []

        for obj in self.objects:
            if obj['handle_id'] not in target_ids:
                continue

            node = self.bam_factory.create(obj['handle_name'], base_name='Texture', bam_version=self.version)
            node.load_object(obj)

            texture = node.transform_to_png(convert_jpg, convert_rgb)

            if texture and texture not in modified_textures:
                modified_textures.append(texture)

            node.write_object(write_version=self.version, obj=obj)

        return modified_textures
