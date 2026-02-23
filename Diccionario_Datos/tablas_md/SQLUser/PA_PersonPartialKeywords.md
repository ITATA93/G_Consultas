# SQLUser.PA_PersonPartialKeywords

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKEYW_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| PKEYW_Alias_DR | varchar |  | FK | SI | Des Ref Alias |
| PKEYW_Childsub | double |  |  | NO | Childsub |
| PKEYW_DOB | date |  |  | SI | DOB |
| PKEYW_EpisodeFlag | varchar |  |  | SI | Episode Flag |
| PKEYW_GNSoundex | varchar |  |  | SI | GNSoundex |
| PKEYW_GivenName | varchar |  |  | SI | GivenName |
| PKEYW_Name | varchar |  |  | SI | Name |
| PKEYW_Name1 | varchar |  |  | SI | Name1 |
| PKEYW_Name2 | varchar |  |  | SI | Name2 |
| PKEYW_ONSoundex | varchar |  |  | SI | ONSoundex |
| PKEYW_OtherName | varchar |  |  | SI | Other Name |
| PKEYW_PatType_DR | bigint |  | FK | SI | Des Ref PatType |
| PKEYW_RowId | varchar |  |  | NO | - |
| PKEYW_Sndx | varchar |  |  | SI | Soundex |
| PKEYW_Sndx1 | varchar |  |  | SI | Sndx1 |
| PKEYW_Sndx2 | varchar |  |  | SI | Sndx2 |
| PKEYW_Soundex | varchar |  |  | SI | Soundex |
| PKEYW_Surname | varchar |  |  | SI | Surname |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*