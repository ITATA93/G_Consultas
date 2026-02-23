# lab.CF_LabtrakPatInquiry

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLPE_ParRef | bigint | PK |  | NO | CF_LabTrak Parent Reference |
| CFLPE_Field_Col | double |  |  | SI | Field Col |
| CFLPE_Field_DR | varchar |  | FK | SI | Field DR |
| CFLPE_Field_Line | double |  |  | SI | Field Line |
| CFLPE_Label_Col | double |  |  | SI | Label Col |
| CFLPE_Label_Line | double |  |  | SI | Label Line |
| CFLPE_Length | varchar |  |  | SI | Length |
| CFLPE_RowID | varchar |  |  | NO | - |
| CFLPE_Sequence | double |  |  | NO | Sequence Number |
| CFLPE_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*