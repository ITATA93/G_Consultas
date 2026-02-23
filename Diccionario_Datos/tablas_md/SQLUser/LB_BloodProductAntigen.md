# SQLUser.LB_BloodProductAntigen

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBBPA_ParRef | bigint | PK |  | NO | Parent Blood Product |
| ChildQ39DR | - |  |  | SI | Child Reference: Abdomen y dorso |
| LBBPA_Antigen_DR | bigint |  | FK | NO | Antigen |
| LBBPA_EntryMode_DR | bigint |  | FK | SI | Mode Of Entry |
| LBBPA_Reaction | varchar |  |  | NO | Reaction |
| LBBPA_RowID | varchar |  |  | NO | - |
| LBBPA_TestSetItem_DR | varchar |  | FK | SI | Test Set item the antigen was derived from |
| Q35Q1 | - |  |  | SI | Percusión |
| Q35Q2 | - |  |  | SI | Auscultación |
| Q35Q3 | - |  |  | SI | Localización |
| Q35Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*