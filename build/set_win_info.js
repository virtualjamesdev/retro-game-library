const ResEdit=require('resedit'); const PE=require('pe-library'); const fs=require('fs');
const [exe,ico]=process.argv.slice(2); const e=PE.NtExecutable.from(fs.readFileSync(exe),{ignoreCert:true}); const res=PE.NtExecutableResource.from(e);
const g=ResEdit.Resource.IconGroupEntry.fromEntries(res.entries)[0];
ResEdit.Resource.IconGroupEntry.replaceIconsForResource(res.entries,g.id,g.lang,ResEdit.Data.IconFile.from(fs.readFileSync(ico)).icons.map(i=>i.data));
let vi=ResEdit.Resource.VersionInfo.fromEntries(res.entries)[0];
if(!vi){vi=ResEdit.Resource.VersionInfo.createEmpty();vi.lang=1033;}
const langs=vi.getAllLanguagesForStringValues();const L=langs[0]||{lang:1033,codepage:1200};
vi.setStringValues(L,{ProductName:'Retro Game Library',FileDescription:'Retro Game Library',CompanyName:'@VirtualJames',InternalName:'Retro Game Library',OriginalFilename:'Retro Game Library.exe',LegalCopyright:'@VirtualJames 2026'});
vi.setFileVersion(1,1,0,0,L.lang);vi.setProductVersion(1,1,0,0,L.lang);vi.outputToResourceEntries(res.entries);res.outputResource(e);fs.writeFileSync(exe,Buffer.from(e.generate()));console.log('set ok',langs);
