# SQLUser.RVI_InsCoBillLocation

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | RVI_InsCompanyBill Parent Reference |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_NFMIDep_DR | varchar |  | FK | SI | Des Ref to NFMIDep |
| LOC_Print | varchar |  |  | SI | Print |
| LOC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*