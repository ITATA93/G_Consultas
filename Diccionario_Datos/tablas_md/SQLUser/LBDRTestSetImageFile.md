# SQLUser.LBDRTestSetImageFile

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRTSI_ParRef | varchar | PK |  | NO | Parent TestSet DR |
| ID | varchar |  |  | NO | - |
| LBDRTSIF_Comments | varchar |  |  | SI | File comments |
| LBDRTSIF_Desc | varchar |  |  | SI | File description |
| LBDRTSIF_Image_DR | bigint |  | FK | SI | websys.document that stores the attachment data (J... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*