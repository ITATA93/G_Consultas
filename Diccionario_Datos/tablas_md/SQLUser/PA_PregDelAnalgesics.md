# SQLUser.PA_PregDelAnalgesics

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANLG_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| ANLG_Analgetic_DR | bigint |  | FK | SI | Des Ref Analgetic |
| ANLG_Childsub | double |  |  | NO | Childsub |
| ANLG_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*