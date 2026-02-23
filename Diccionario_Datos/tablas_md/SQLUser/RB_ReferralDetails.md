# SQLUser.RB_ReferralDetails

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | RB_Referral Parent Reference |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_Header | varchar |  |  | SI | Header |
| DET_Level | varchar |  |  | SI | Level |
| DET_RowId | varchar |  |  | NO | - |
| DET_Text | varchar |  |  | SI | Text |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*