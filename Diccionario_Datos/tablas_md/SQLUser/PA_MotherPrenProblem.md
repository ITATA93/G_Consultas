# SQLUser.PA_MotherPrenProblem

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PREP_Childsub | double | PK |  | NO | Childsub |
| PREP_ParRef | bigint | PK |  | NO | PA_Mother Parent Reference |
| PREP_PrenProbl_DR | bigint | PK | FK | SI | Des Ref to PrenProbl |
| PREP_RowId | varchar | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*