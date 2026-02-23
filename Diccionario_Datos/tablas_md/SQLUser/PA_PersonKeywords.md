# SQLUser.PA_PersonKeywords

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| KEYW_Alias_DR | varchar |  | FK | SI | Des Ref Alias |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_DOB | date |  |  | SI | DOB |
| KEYW_EpisodeFlag | varchar |  |  | SI | Episode Flag |
| KEYW_GNSoundex | varchar |  |  | SI | GNSoundex |
| KEYW_GivenName | varchar |  |  | SI | GivenName |
| KEYW_Name | varchar |  |  | SI | Name |
| KEYW_Name1 | varchar |  |  | SI | Name1 |
| KEYW_Name2 | varchar |  |  | SI | Name2 |
| KEYW_ONSoundex | varchar |  |  | SI | ONSoundex |
| KEYW_OtherName | varchar |  |  | SI | Other Name |
| KEYW_PatType_DR | bigint |  | FK | SI | Des Ref PatType |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Sndx | varchar |  |  | SI | Soundex |
| KEYW_Sndx1 | varchar |  |  | SI | Sndx1 |
| KEYW_Sndx2 | varchar |  |  | SI | Sndx2 |
| KEYW_Soundex | varchar |  |  | SI | Soundex |
| KEYW_Surname | varchar |  |  | SI | Surname |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*