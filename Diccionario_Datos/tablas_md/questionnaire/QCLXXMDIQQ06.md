# questionnaire.QCLXXMDIQQ06

> Mantención Dispositivos Invasivos : Dispositivos Vías Urinarias

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mantención Dispositivos Invasivos : Dispositivos Vías Urinarias

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | varchar |  |  | SI | Tipo de Dispositivos |
| Q06Q2 | varchar |  |  | SI | Actividad |
| Q06Q3 | varchar |  |  | SI | Tamaño |
| Q06Q4 | varchar |  |  | SI | Ubicación |
| Q06Q5 | varchar |  |  | SI | N° Días Dispositivo Vías Urinaria |
| Q06Q6 | varchar |  |  | SI | ¿Es necesario el DI? |
| Q06Q7 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*