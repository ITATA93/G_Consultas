# SQLUser.PA_WaitingListAdditDiag

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADIAG_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| ADIAG_Childsub | double |  |  | NO | Childsub |
| ADIAG_ICD_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| ADIAG_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*